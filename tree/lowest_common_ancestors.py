#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1134375821/

#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# similar solution for both the LCA of a BT and BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        qu = deque()
        parent={}
        if root:
            qu.append(root)
            parent[root]=None
        while qu:
            curr = qu.popleft()
            if curr.left:
                qu.append(curr.left)
                parent[curr.left]=curr
            if curr.right:
                qu.append(curr.right)
                parent[curr.right]=curr
        
        ancestor =set()
        while q:
            ancestor.add(q)
            q = parent[q]

        while p:
            if p in ancestor:
                return p
            p = parent[p]
        