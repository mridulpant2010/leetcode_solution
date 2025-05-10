from collections import defaultdict
import heapq
def least_interval(tasks,n):
    d = defaultdict(int)
    max_gaps=0
    for each_task in tasks:
        d[each_task]+=1
        max_gaps = max(max_gaps,d[each_task])
    
    he=[]
    max_gaps-=1
    idleslots=max_gaps*(n+1)
    for k,v in d.items():
        heapq.heappush(he,(-v,k))
    
    while len(he)>0:
        v,k=heapq.heappop(he)
        v=-v
        idleslots-=min(max_gaps,v)
    if idleslots<0:
        idleslots=0
    print(idleslots+len(tasks))

if __name__=="__main__":
    #tasks=["A","A","A","B","B","B"]
    #n=2
    tasks=["A","A","B","B"]
    n=2
    least_interval(tasks,n)