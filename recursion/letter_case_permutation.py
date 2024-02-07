class Solution:
    
    def __init__(self):
        self.res=[]
    
    def letterCasePermutations(self,ip,op):
        if len(ip)==0:
            self.res.append(op)
            return 
        op1=op
        op2=op
        if ip[0].isalpha():

            op1=op1+ip[0].lower()
            op2=op2+ip[0].upper()
            ip=ip[1:]
            self.letterCasePermutations(ip,op1)
            self.letterCasePermutations(ip,op2)
        else:
            op1=op1+ip[0]
            ip=ip[1:]
            self.letterCasePermutations(ip,op1)
        return
    def letterCasePermutation(self, S: str) -> List[str]:
        self.letterCasePermutations(S,'')
        return self.res
        