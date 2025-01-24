
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinarySearchTree:
    def __init__(self,val):
        self.root = TreeNode(val)
        self.left='left'
        self.right='right'
        
        
    def _insert(self,root,value,parent,ident):
        if root is not None:
            if value < root.data:
                self._insert(root.left,value,root,'left')
                #right side 
            else:
                self._insert(root.right,value,root,'right')
        else:
            if ident == self.left: 
                parent.left = TreeNode(value)
            else:
                parent.right=TreeNode(value)
        return

    def inorder_traversal(self,node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end = " ")
            self.inorder_traversal(node.right)
    
                
# Example usage
bst = BinarySearchTree(10)
bst._insert(bst.root,5,bst.root,None)
bst._insert(bst.root,15,bst.root,None)
bst._insert(bst.root,2,bst.root,None)
bst._insert(bst.root,7,bst.root,None)
bst._insert(bst.root,12,bst.root,None)
bst._insert(bst.root,20,bst.root,None)

print("Inorder Traversal:")
bst.inorder_traversal(bst.root)
print()


#there is a way that you can improve this code and can make it better, please check that.