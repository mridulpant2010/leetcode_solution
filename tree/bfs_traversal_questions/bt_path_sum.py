#from TreeNode import TreeNode
from collections import defaultdict,deque
from itertools import chain
import importlib
import importlib.util


def import_module_from_spec(module_spec):
    module=importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module 

def dynamic_import(module):
    return importlib.import_module(module)

def bt_path_sum(root,path_sum):
    #returns True if the path exists otherwise returns false
    if root is None: return False
    if root.left is None and root.right is None: 
        if root.val==path_sum:#-root.val:
            return True
    
    a=bt_path_sum(root.left,path_sum-root.val)
    b=bt_path_sum(root.right,path_sum-root.val)
    return a or b




def bt_path(root,sum_of_path,current_path,all_paths):
    #provides all the path from the root to leaf such that sum of all the node values of each path ='S' 
    

    if root is None: return 
    current_path.append(root.val)
    if root.left is None and root.right is None and root.val==sum_of_path:
        all_paths.append(list(current_path))
    #else:
    a = bt_path(root.left,sum_of_path-root.val,current_path,all_paths)
    b = bt_path(root.right,sum_of_path-root.val,current_path,all_paths)

    del current_path[-1]
    #return 
    
if __name__ == '__main__':
    
    #we are doing input with in the level_order_traversal.
    '''
    a = list(map(int,input().split()))
    c=chain(a)
    path_sum = int(input())
    #print(a)
    root=TreeNode.buildLevelOrder(c)
    #print(TreeNode.printPreorder(root))
    print(TreeNode.LevelOrderTraversal(root))
    
    ans=bt_path_sum(root,path_sum)
    print(ans)
    '''
    #TreeNode=dynamic_import('TreeNode')
    TreeNode = import_module_from_spec('TreeNode')
    
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print(TreeNode.LevelOrderTraversal(root))
    #print("Tree has path: " + str(bt_path_sum(root, 23)))
    #print("Tree has path: " + str(bt_path_sum(root, 16)))
    
    all_paths=[]
    bt_path(root,required_sum,[],all_paths)
    print(*all_paths)