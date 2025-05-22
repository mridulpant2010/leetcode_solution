#https://github.com/mridulpant2010/grokking_coding_interview/blob/main/top_K_elements/Frequency%20Sort%20(medium)%20-%20Grokking%20the%20Coding%20Interview_%20Patterns%20for%20Coding%20Questions.pdf
import heapq
from collections import defaultdict
def frequency_sort(strn):
    d=defaultdict(int)
    he=[]
    for i in range(len(strn)):
        d[strn[i]]+=1
    
    for k,v in d.items():
        heapq.heappush(he,(-v,k))
    
    while len(he)>0:
        ans=heapq.heappop(he)
        print(ans[1]*(-ans[0]),end="")
        #print(ans[0],ans[1])
    print()
        
frequency_sort("Programming")
frequency_sort("abcbab")