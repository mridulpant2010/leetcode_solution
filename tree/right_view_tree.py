
'''
given a tree you need to print its right view
'''
from collections import deque 
from typing import List



class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left 
        self.right=right

def tree_right_view(root):
    res=[]
    q=deque()
    q.append(root)
    while q:
        depthsize=len(q)
        for i in range(depthsize):
            currentNode=q.popleft()
            
            if i==depthsize-1:
                res.append(currentNode.val)
                
            if currentNode.left:
                q.append(currentNode.left)
                
            if currentNode.right:
                q.append(currentNode.right)
    return res


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node) + " ", end='')