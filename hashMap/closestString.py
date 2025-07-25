from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in word1:
            d1[c]+=1
        for i in word2:
            d2[i]+=1
        print(d1.values(),d2.values())
        print(sorted(d1.keys()),sorted(d2.keys()))
        return sorted(d1.values())==sorted(d2.values()) and sorted(d1.keys())==sorted(d2.keys())  

if __name__ == "__main__":
    s= Solution()
    word1="abc"
    word2= "bca"
    ans = s.closeStrings(word1,word2)
    print(ans)