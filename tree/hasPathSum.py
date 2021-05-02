#leetcode question: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
  # TODO: Write your code here
  
  if root is None :
    return False
  
  if root.left is None and root.right is None and root.val==sum:
    return True

  if root is not None:
    a=has_path(root.left,sum-root.val)
    b=has_path(root.right,sum-root.val)
    return a or b


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
