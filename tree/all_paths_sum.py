#https://www.educative.io/courses/grokking-the-coding-interview/B815A0y2Ajn

'''
solution to thea
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
      
  if root is None:
      return 
  
  if root.left is None and root.right is None and root.val==sum:
      pass
  if root is not None:
      find_paths(root.left, sum-root.val)
      find_paths(root.right, sum-root.val)
      #return a or b
  return 

if __name__ == '__main__':
    allPaths=[]
    count=0
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))

