#https://leetcode.com/problems/letter-case-permutation/
def letterCasePermutation(ip,op):
    if len(ip)==0:
        print(op)
        return 
    op1=op
    op2=op
    if ip[0].isalpha():
        
        op1=op1+ip[0].lower()
        op2=op2+ip[0].upper()
        ip=ip[1:]
        letterCasePermutation(ip,op1)
        letterCasePermutation(ip,op2)
    else:
        op1=op1+ip[0]
        ip=ip[1:]
        letterCasePermutation(ip,op1)
    return

if __name__=='__main__':
    letterCasePermutation('a1b2','')