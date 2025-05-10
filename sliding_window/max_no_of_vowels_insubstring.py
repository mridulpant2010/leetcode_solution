#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/1520944620/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        string_len = len(s)
        start=0
        end = 0
        vowel_count = 0
        max_vowel_count = 0
        while end < string_len:
            if s[end] in vowels:
                vowel_count+=1
            if end-start+1==k:
                max_vowel_count = max(max_vowel_count,vowel_count)
                if s[start] in vowels:
                    vowel_count-=1
                start+=1
            end+=1
        return max_vowel_count