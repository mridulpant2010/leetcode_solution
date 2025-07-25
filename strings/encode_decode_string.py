from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for el in strs:
            el_len=len(el)
            s+= str(el_len)+"#"+el
        return s


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]; mul=10; 
        while i<len(s):
            digit=0
            while s[i]!="#":
                digit = digit*mul +int(s[i])
                i+=1
            start=i+1
            end = i+digit
            new_s=""
            while start<=end :
                new_s+=s[start]
                print(start,new_s,res)
                start+=1
                
            i=end+1
            res.append(new_s)
        return res


if __name__ == "__main__":
    s = Solution()
    strs = ["we","say",":","yes","!@#$%^&*()"]
    res=s.encode(strs)
    print(res)
    ans = s.decode(res)
    print(ans)