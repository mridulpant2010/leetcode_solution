def replace_pi(ip,op):
    if len(ip)==0:
        print(op,end='')
        return
    
    op1=op
    if ip[0]=='p' and ip[1]=='i' and len(ip)>=2:
        op1=op1+'3.14'
        ip=ip[2:]
        replace_pi(ip,op1)
    else:
        op1=op1+ip[0]
        ip=ip[1:]
        replace_pi(ip,op1)
    return 
        
if __name__ == "__main__":
    t=int(input())
    while t:
        a=input()
        replace_pi(a,"")
        print()
        t-=1