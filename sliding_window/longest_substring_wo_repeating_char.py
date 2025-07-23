from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        start =0 
        max_len = 0
        d = defaultdict(int)
        while end < len(s):
            d[s[end]]+=1
            while end-start+1 > len(d.keys()):
                d[s[start]]-=1
                if d[s[start]]==0:
                    del d[s[start]]
                start+=1
            max_len = max(max_len,end-start+1)
            end+=1
        return max_len      
            
            
if __name__ == "__main__":
    s = Solution()
    st="pwwkew"#"abcabcbb"
    ans = s.lengthOfLongestSubstring(st)
    print(ans)