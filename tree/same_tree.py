#https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            currNode = q1.popleft()
            currNode2 = q2.popleft()
            if (currNode is None and currNode2 is not None) or (currNode is not None and currNode2 is None):
                return False
            if currNode and currNode2:           
                if currNode.val!=currNode2.val:
                    return False
                q1.append(currNode.left)
                q1.append(currNode.right)
                q2.append(currNode2.left)
                q2.append(currNode2.right)
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first=deque()
        second =deque()
        first.append(p)
        second.append(q)
        res1=[]
        res2=[]
        while first:
            curr = first.popleft()
            if curr:
                res1.append(curr.val)
                first.append(curr.left)
                first.append(curr.right)
            else:
                res1.append(None)
        
        while second:
            curr = second.popleft()
            if curr:
                res2.append(curr.val)
                second.append(curr.left)
                second.append(curr.right)
            else:
                res2.append(None)
            
        return res1==res2
        