# https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked
from collections import defaultdict
class Solution:

    def getCount(self,p):
        d = defaultdict(int)
        for char in p:
            d[char]+=1
        return d

    def findAnagrams(self, s: str, p: str) -> List[int]:
        curr = 0
        str_len = len(s)
        anagram_len = len(p)
        start=0
        result=[]
        d = self.getCount(p)
        match_d=defaultdict(int)
        while curr< str_len:
            #print(curr,s[curr],start)
            if s[curr] not in d.keys():
                match_d.clear()
                start=curr+1
            else:
                match_d[s[curr]] += 1

            #print(curr,match_d)
            if curr-start+1 == anagram_len:
                if d == match_d:
                    #sum(d.values())==0:
                    print(curr,start)
                    result.append(start)
                    #d = self.getCount(p)
                
                if s[start] in match_d.keys():
                    match_d[s[start]]-=1
                    if match_d[s[start]] == 0:
                        del match_d[s[start]]
                start+=1
            curr+=1
        return result

        