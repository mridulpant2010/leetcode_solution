#https://leetcode.com/problems/valid-parenthesis-string/submissions/1692708586/
class Solution:
    def checkValidString(self, s: str) -> bool:
        low_bound = 0 ; high_bound = 0
        end = 0
        while end < len(s):
            if s[end]=='(':
                low_bound+=1
                high_bound+=1
            elif s[end]==')':
                low_bound-=1
                high_bound-=1
            elif s[end]== "*":
                low_bound-=1
                high_bound+=1
            if low_bound < 0:
                low_bound=0
            if high_bound <0:
                return False
            end+=1
        return low_bound ==0
        