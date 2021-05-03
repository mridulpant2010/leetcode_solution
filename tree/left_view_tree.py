from collections import deque
from itertools import chain


class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        
        
def buildTree_levelorder(ip):
    #to peform the level order traversal we have to use the quee
    q=deque()
    root=TreeNode(next(ip))
    q.append(root)
    while q:
        currentNode=q.popleft()
        c1=next(ip)
        c2=next(ip)
        
        if c1!=-1:
            currentNode.left = TreeNode(c1)
            q.append(currentNode.left)

        if c2!=-1:
            currentNode.right=TreeNode(c2)
            q.append(currentNode.right)
    return root


def printTree(root):
    if root is None: return
    print(root.val)
    printTree(root.left)
    printTree(root.right)
    

def leftViewTree(root):
    q=deque()
    q.append(root)
    res=[]
    while q:
        depthsize=len(q)
        for i in range(depthsize):
            currentNode=q.popleft()  
            
            if i==0:
              res.append(currentNode.val)
            if currentNode.left:
                q.append(currentNode.left) 
            if currentNode.right:
                q.append(currentNode.right)
        #res.append(currentList)
    return res

if __name__ == '__main__':
    a= list(map(int,input().split()))
    c= chain(a)
    root=buildTree_levelorder(c)
    #printTree(root)
    res=leftViewTree(root)
    print(*res)