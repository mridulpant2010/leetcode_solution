
from collections import deque
class TreeNode:
    
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def find_min_depth(root):
    q=deque()
    q.append(root)
    depthsize=0
    while q:
        currsize=len(q)
        depthsize+=1
        for _ in range(currsize):
            currentNode=q.popleft()
            if currentNode.left is None and currentNode.right is None:
                return depthsize
            if currentNode.left:
                q.append(currentNode.left)        
            if currentNode.right:
                q.append(currentNode.right)
    return depthsize


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(find_min_depth(root))
