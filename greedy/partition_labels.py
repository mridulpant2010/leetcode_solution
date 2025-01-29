#https://leetcode.com/problems/partition-labels/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_rightindex={char:index for index,char in enumerate(s)} #capture the rightmost index of the string
        result=[]
        left , right = 0 , 0
        for i in range(len(s)):
            current_char = s[i]
            right = max(right,char_rightindex[current_char]) #get the rightmost index from the partition 
            #if your i has reached the rightmost index then add to result
            if i == right:
                result.append(right-left+1)
                left = i+1
        return result        