#https://leetcode.com/problems/insert-interval/

def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    mergedInterval = []
    #previous adding to the mergedInterval
    i=0
    for i in range(len(intervals)):
        if newInterval[0]<=intervals[i][1]:
            break
        else:
            mergedInterval.append(intervals[i])
    #merge process and checking the overlapping condition
    while i < len(intervals) and newInterval[1]>= intervals[i][0]:
        newInterval[0] = min(newInterval[0],intervals[i][0])
        newInterval[1] = max(newInterval[1],intervals[i][1])
        print(newInterval)
        i+=1
    mergedInterval.append(newInterval)
    while i < len(intervals):
        mergedInterval.append(intervals[i])
        i+=1
    return mergedInterval

if __name__=='__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
    newInterval = [4,8]
    ans = insert(intervals, newInterval)    
    print(ans)
    
    intervals = [[1,5]]
    newInterval = [5,7]
    ans2 = insert(intervals, newInterval)
    print(ans2)
    
    intervals = [[1,5]]
    newInterval = [6,8]
    ans3 = insert(intervals, newInterval)
    print(ans3)