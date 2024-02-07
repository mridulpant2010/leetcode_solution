# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        current=root
        while current:
            if current.left:
                last = current.left
                while last.right:
                    last=last.right
                last.right=current.right
                current.right=current.left
                current.left=None
            current=current.right
        return root
        

        