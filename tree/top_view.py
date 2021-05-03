from collections import namedtuple,deque,defaultdict
from itertools import chain

class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def levelOrderTraversal(root):
    q=deque()
    res=[]
    q.append(root)
    while q:
        depthsize=len(q)
        currentList=[]
        for _ in range(depthsize):
            currentNode=q.popleft()
            #print(1,currentNode.val)
            currentList.append(currentNode.val)
            if currentNode.left:
                q.append(currentNode.left)
                
            if currentNode.right:
                q.append(currentNode.right)
        res.append(currentList)
    return res
    
def buildlevelOrder(ip):
    q=deque()
    root=TreeNode(next(ip))
    q.append(root)
    while q:
        currentNode = q.popleft()
        
        c1=next(ip)
        c2=next(ip)
        if c1!=-1:
            currentNode.left=TreeNode(c1)
            q.append(currentNode.left)
        
        if c2!=-1:
            currentNode.right=TreeNode(c2)
            q.append(currentNode.right)
                    
    return root


def printLevelOrder(root):
    if root is None: return 
    print(root.val)
    printLevelOrder(root.left)
    printLevelOrder(root.right)

def topview(root):
    '''
    concept of calculating the horizontal distance
    1- hd of root=0
    2- hd of leftchild = hd of parent-1
    3- hd of rightchild = hd of parent+1
    '''
    if root is None: return 
    set_map=defaultdict(int)
    q=deque()
    mi= float('inf')
    q.append((0,root))
    while q:
        currentNode=q.popleft()
        hd =currentNode[0]
        val=currentNode[1].val
        if hd not in set_map.keys():
            set_map[hd]=val
            mi = min(mi,hd)
        if currentNode[1].left :
            q.append((hd-1,currentNode[1].left))
        if currentNode[1].right:
            q.append((hd+1,currentNode[1].right))
    
    while mi in set_map:
        print(set_map[mi],end=' ')
        mi+=1
    #return[ v for k,v in set_map.items() ]
        #print(k,v)

def bottomview(root):
    if root is None: return 
    set_map=defaultdict(int)
    q=deque()
    mi= float('inf')
    q.append((0,root))
    while q:
        currentNode=q.popleft()
        hd =currentNode[0]
        val=currentNode[1].val
        #if hd in set_map.keys():
        set_map[hd]=val
        mi = min(mi,hd)
        if currentNode[1].left :
            q.append((hd-1,currentNode[1].left))
        if currentNode[1].right:
            q.append((hd+1,currentNode[1].right))
    
    while mi in set_map:
        print(set_map[mi],end=' ')
        mi+=1
    
    #pass

if  __name__ == '__main__':
    
    a= list(map(int,input().split()))
    c= chain(a)
    root=buildlevelOrder(c)
    #printLevelOrder(root)
    res=levelOrderTraversal(root)
    bottomview(root)
    #print(*res)
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.right = TreeNode(6)
    #root.right.left.left = TreeNode(20)
    #root.right.left.right = TreeNode(17)
    '''
    #res=levelOrderTraversal(root)
    #print(*res)