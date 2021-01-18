class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



    
def buildTree():
    data=int(input())
    if data==-1:
        return None
    
    root= Node(data)
    root.left=buildTree()
    root.right=buildTree()
    return root

def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)


if __name__=='__main__':
    root=buildTree()
    printTree(root)
    