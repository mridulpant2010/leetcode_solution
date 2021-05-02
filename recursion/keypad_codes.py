#question-link: https://online.codingblocks.com/app/player/173171/content/173393/4890/code-challenge

def keypad_codes(ip,op,i,n):
    
    #base-case
    if i==n:
        output.append(''.join(op))
        return 
    
    #recursive-case 
    digit=int(ip[i])
    for k in range(len(hash_table[digit])):
        op.append(hash_table[digit][k])
        keypad_codes(ip,op,i+1,n)
        op.pop()


if __name__ == '__main__':
    output=[]
    hash_table= [" ", "abc", "def", "ghi", "jkl" , "mno", "pqrs" , "tuv", "wx","yz"]
    n= input()
    keypad_codes(n,[],0,len(n))
    print(*output)
    print(len(output))