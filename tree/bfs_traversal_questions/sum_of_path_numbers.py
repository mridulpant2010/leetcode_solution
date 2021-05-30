from TreeNode import TreeNode

def sum_of_path_numbers(root,curr_digit,final_sum):
    if root is None: return 0
    
    curr_digit=curr_digit*10+root.val
    if root.left is None and root.right is None:          
        final_sum =final_sum+curr_digit
        return final_sum
    a=sum_of_path_numbers(root.left,curr_digit,final_sum)
    b=sum_of_path_numbers(root.right,curr_digit,final_sum)
    return a+b
    #curr_digit= int((curr_digit-root.val)//10)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    
    final_sum=0
    res=sum_of_path_numbers(root,0,final_sum)
    print(res)