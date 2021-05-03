from collections import deque
from typing import List
from itertools import chain
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def buildTree(ip) -> None:
    data=next(ip)
    if data==-1:
        return None
    
    root= Node(data)
    root.left=buildTree(ip)
    root.right=buildTree(ip)
    return root

def printTree(root: List[Node]) -> None:
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)


def bfstraversal(root: List[Node]) -> list:
    q=deque()
    q.append(root)
    res=[]
    while q:
        depthsize=len(q)
        currentResult=deque()
        for _ in range(depthsize):
            currentNode=q.popleft()
            
            currentResult.append(currentNode.data)
            
            if currentNode.left:
                q.append(currentNode.left)

            if currentNode.right:
                q.append(currentNode.right)
        
        res.append(list(currentResult))
    return res
    
                    
if __name__=='__main__':
    a=list(map(int,input().split()))
    
    #converting a list into the generator
    c=chain(a)
    root=buildTree(c)
    printTree(root)

    res=bfstraversal(root)
    print(res)