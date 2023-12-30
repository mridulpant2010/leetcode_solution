import heapq

def maximum_cpu_load(intervals):
    intervals.sort(key=lambda x:x[0])
    max_cpu_load = 0
    he=[]
    heapq.heapify(he)
    start=0
    curr_load_time=0
    while start < len(intervals):
        curr = intervals[start]
        while len(he)>0 and he[0][0]<=curr[0]:
            el_pop = heapq.heappop(he)
            curr_load_time -= el_pop[2]
        heapq.heappush(he,[curr[1],curr[0],curr[2]])
        curr_load_time += curr[2]
        max_cpu_load = max(max_cpu_load, curr_load_time)
        start+=1
    return max_cpu_load

if __name__ == '__main__':
    intervals = [[1,4,3],[2,5,4],[7,9,6]]
    ans = maximum_cpu_load(intervals)
    print(ans)

    intervals = [[6,7,10],[2,4,11],[8,12,15]]
    ans = maximum_cpu_load(intervals)
    print(ans)
    
    intervals = [[1,4,2],[2,4,1],[3,6,5]]
    ans = maximum_cpu_load(intervals)
    print(ans)