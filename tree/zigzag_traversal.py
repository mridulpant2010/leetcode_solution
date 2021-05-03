'''
Given a binary tree. Print the zig zag order i.e print level 1 from left to right, 
level 2 from right to left and so on. 
This means odd levels should get printed from left to right and even levels should be printed from right to left.

Input Format
Enter the values of all the nodes in the binary tree in pre-order format where true suggest the node exists and false suggests it is NULL
'''


from typing import List 
from collections import deque
from itertools import chain


class Node:
    
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
        

def buildTree(ip) -> None:
    data=next(ip)
    #print(data)
    if data == 'true':
        data=next(ip)
        
    elif data=='-1':#'false':
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



def bfstraversal(root: List[Node]) -> None:
    
    q=deque()
    res=[]
    q.append(root)
    leftToRight=True
    while q:
        depthsize=len(q)
        currentList=deque()
        for _ in range(depthsize):
            currentNode=q.popleft()
            if leftToRight:
                currentList.append(currentNode.data)
            else:
                currentList.appendleft(currentNode.data)        
            
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        leftToRight= not leftToRight
        res.extend(list(currentList)) 
    return res           

if __name__ == '__main__':
    a=list(map(str,input().split()))
    c=chain(a)
    root=buildTree(c)
    printTree(root)
    print(*bfstraversal(root))