from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        
        
def find_successor(root,key):
    
    if root is None: return None
    q=deque()
    q.append(root)
    
    while q:
        currentNode=q.popleft()
        if currentNode.left:
            q.append(currentNode.left)
        if currentNode.right:
            q.append(currentNode.right)
        if currentNode.val== key:
            break
        
    return q[0] if q else None


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)