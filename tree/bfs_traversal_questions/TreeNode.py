from collections import deque
from typing import List

#when do we decide for the static method and when do we decide for the classmethod



class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    
    @staticmethod
    def buildLevelOrder(ip) :
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

    @staticmethod
    def printPreorder(root) :
        if root is None: return
        print(root.val)
        TreeNode.printPreorder(root.left) #we are doing recursion inside the staticmethod
        TreeNode.printPreorder(root.right) 
        
    @staticmethod
    def LevelOrderTraversal(root):
        q=deque()
        q.append(root)
        res=[]
        while q:
            depthsize=len(q)
            currentResult=[]
            for _ in range(depthsize):
                currentNode=q.popleft()
                
                currentResult.append(currentNode.val)
                if currentNode.left:
                    q.append(currentNode.left)
                    
                if currentNode.right:
                    q.append(currentNode.right)
            res.append(currentResult)
        return res
        