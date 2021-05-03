from collections import deque
from itertools import chain

class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        

def buildTreeLevelOrder(ip):
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
    

def printTree(root):
    if root is None: return 
    print(root.val)
    printTree(root.left)
    printTree(root.right)



def rightViewTree(root):
    q=deque()
    res=[]
    q.append(root)    
    while q:
        depthsize=len(q)
        for i in range(depthsize):        
            currentNode=q.popleft()   
            #print(currentNode.val)
            if i==depthsize-1: 
                res.append(currentNode.val)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
    return res



if __name__=='__main__':
    a = list(map(int,input().split()))
    c=chain(a)
    root=buildTreeLevelOrder(c)
    res=rightViewTree(root)
    #printTree(root)
    print(*res)