def subset_sum(ip,op):
    if len(ip)==0:
        print(op)
        return 
    
    op1=op
    op2=op
    op2=ip[0]+op2
    ip1=ip[1:]
    subset_sum(ip1,op1)
    subset_sum(ip1,op2)
    return
    
    
if __name__ == '__main__':
    l = '13'
    subset_sum(l,'')
