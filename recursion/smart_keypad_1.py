def smart_keypad(ip,op,i,n):
    #base-case 
    if i==n:
        print(''.join(op))
        return 
    
    #recursive case
    digit= int(ip[i])
    if digit==0: 
        smart_keypad(ip,op,i+1,n)
    
    for k in range(len(hash_table[digit])):
        op.append(hash_table[digit][k])
        smart_keypad(ip,op,i+1,n)
        op.pop()
    
        


if __name__=='__main__':
    hash_table= [" ", ".+@$", "abc", "def", "ghi", "jkl" , "mno", "pqrs" , "tuv", "wxyz"]
    n = input()
    smart_keypad(n,[],0,len(n))
    