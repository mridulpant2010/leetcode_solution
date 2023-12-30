#https://leetcode.com/problems/remove-covered-intervals/description/

def removeCoveredIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    count=0
    intervals.sort(key=lambda x: (x[0],-x[1]))
    print(intervals)
    start=1
    last = intervals[0]
    while start<len(intervals):
        curr = intervals[start]
        if (last[0]<=curr[0] and curr[1]<=last[1]):
            count+=1
        else:
            last=curr
        start+=1
    return len(intervals)-count

if __name__ == "__main__":
    intervals=[[1, 4], [2, 8], [3, 6]]
    ans = removeCoveredIntervals(intervals)
    print(ans) 