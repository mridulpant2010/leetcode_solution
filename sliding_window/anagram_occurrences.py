#https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
from collections import defaultdict
def search(pat, txt):
    # code here
    end =0
    start=0
    len_pat = len(pat)
    ans=0
    hash_map = defaultdict(int)
    for i in pat:
        hash_map[i]+=1
    count = len(hash_map.keys())
    #print(count,hash_map.keys(),len_pat)
    while end < len(txt):
        if txt[end] in hash_map:
            hash_map[txt[end]]-=1
            if hash_map[txt[end]]==0:
                count-=1
        if end-start+1 < len_pat:
            end+=1
        elif end-start+1==len_pat:
            if count==0:
                ans+=1
            if txt[start] in hash_map:
                hash_map[txt[start]]+=1
                if hash_map[txt[start]]==1:
                    count+=1
            start+=1
            end+=1
    return ans
 
 
def anagram_occurrences(txt,pat):
    d=defaultdict(int)
    pattern_d=defaultdict(int)
    count=0
    end=0;start=0; k = len(pat)
    for c in pat:
        pattern_d[c]+=1
    print(pattern_d)
    while end<len(txt):
        d[txt[end]]+=1
        print(end,d)
        if end-start+1==k:
            if d==pattern_d:
                print(d)
                count+=1
            d[txt[start]]-=1
            if d[txt[start]]==0:
                del d[txt[start]]
            start+=1
        end+=1
    return count
    
    
 
if __name__=="__main__":
    # txt = "forxxorfxdofr"
    # pat = "for"
    txt = "aabaabaa"
    pat = "aaba"
    ans=search(pat,txt)
    ans2 = anagram_occurrences(txt,pat)
    print(ans)
    print(ans2)