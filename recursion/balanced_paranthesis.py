
def balanced_paranthesis(op,ip_b,cl_b,n):
    #base-condition
    if ip_b == n and cl_b==n:
        print(op)
        return 
    op1=op
    op2=op
    
    if ip_b <n:
        op1=op1+'('
        balanced_paranthesis(op1,ip_b+1,cl_b,n)
    
    if cl_b < ip_b :
        op2=op2+')'
        balanced_paranthesis(op2,ip_b,cl_b+1,n)
    
    return
    
    
if __name__ == '__main__':
    balanced_paranthesis('',0,0,3)