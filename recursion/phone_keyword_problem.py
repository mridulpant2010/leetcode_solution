def generate_numbers(ip,op,i,n):    
    #base case
    if i==n:
        print(*op)
        return
    
    digit = int(ip[i])
    
    #handling the special case for the digit=0 and digit=1
    if digit ==0  or digit==1:
        generate_numbers(ip,op,i+1,n)
    
    #recursive case    
    for k in range(len(hash_table[digit])):
        op.append(hash_table[digit][k])
        generate_numbers(ip,op,i+1,n)
        op.pop()

if __name__ == "__main__":
    hash_table=[" ", ".+@$", "abc", "def", "ghi", "jkl" , "mno", "pqrs" , "tuv", "wxyz"]
    #['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    
    generate_numbers(['1','2'],[],0,2)