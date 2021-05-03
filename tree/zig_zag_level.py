from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        
def traverse(root):
    res=[]
    q=deque()
    q.append(root)
    leftToRight=True
    while q:
        lensize=len(q)
        currentResult=deque()
        for i in range(lensize):
            currentNode=q.popleft()
            if  leftToRight: #lensize %2==0:
                currentResult.append(currentNode.val) 
            else:
                currentResult.appendleft(currentNode.val)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        
        res.append(list(currentResult))    
        leftToRight = not leftToRight
    return res
    
    
if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    
    print("level order traversal ")
    print(traverse(root))