
import heapq
class Interval:
    def __init__(self,start,end):
        self.start_time=start
        self.end_time=end 



def employee_free_time(interval):
    he=[]
    for i in range(len(interval)):
        heapq.heappush(he,(interval[i][0].start_time,i,0))
        print(interval[i][0].start_time,i,0)
    print(he)
    previous = he[0][0]
    result=[]
    while he :
        _,i,j = heapq.heappop(he)
        curr_interval = interval[i][j]
        if previous < curr_interval.start_time:
            result.append([previous,curr_interval.start_time])
        previous = max(previous,curr_interval.end_time)
        
        if j+1 < len(interval[i]):
            heapq.heappush(he,(interval[i][j+1].start_time,i,j+1))
    return result

if __name__ == "__main__":
    interval = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]] 
    # inputs = [
    #     [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]],
    #     [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]],
    #     [[Interval(2, 3), Interval(7, 9)], [Interval(1, 4), Interval(6, 7)]],
    #     [[Interval(3, 5), Interval(8, 10)], [Interval(4, 6), Interval(9, 12)], [Interval(5, 6), Interval(8, 10)]],
    #     [[Interval(1, 3), Interval(6, 9), Interval(10, 11)], [Interval(3, 4), Interval(7, 12)], [Interval(1, 3), Interval(7, 10)], [Interval(1, 4)], [Interval(7, 10), Interval(11, 12)]],
    #     [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8)], [Interval(2, 3), Interval(4, 5), Interval(6, 8)]],
    #     [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)]]

    # ]
    ans=employee_free_time(interval) 
    print(ans)