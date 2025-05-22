#https://leetcode.com/problems/reorganize-string/
import heapq
from collections import defaultdict

def rearrange_string(stri):
    d=defaultdict(int)
    for i in range(len(stri)):
        d[stri[i]]+=1
    
    he=[]
    for k,v in d.items():
        heapq.heappush(he,(-v,k))
    
    prevChar=None;prevFreq=0
    result=[]
    while len(he)>0:
        currFreq,currChar=heapq.heappop(he)
        if prevChar and -prevFreq>0:
            heapq.heappush(he,(prevFreq,prevChar))
        result.append(currChar)
        prevChar=currChar
        prevFreq=currFreq+1
    return "".join(result) if len(result)==len(stri) else ""
        

print(rearrange_string("aappp"))
                