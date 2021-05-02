from collections import deque

class TreeNode:
    
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        

def traverse(root):
    res=[]
    q=deque()
    q.append(root)
    while q:
        levelSize=len(q)
        currentResult=[]
        for _ in range(levelSize):
            currentNode=q.popleft()
            currentResult.append(currentNode.val)
            
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        res.append(currentResult)
    return res


if __name__ == "__main__":
    root=TreeNode(12)
    root.left=TreeNode(7)
    root.right=TreeNode(1)
    root.left.left=TreeNode(9)
    root.right.right=TreeNode(10)
    root.right.right=TreeNode(5)
    
    print("level order traversal ")
    print(traverse(root))

        