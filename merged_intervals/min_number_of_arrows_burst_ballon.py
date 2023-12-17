#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150

def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort(key=lambda x:x[1])
    start=0
    end=1
    count=1
    while end < len(points):
        curr_el=points[end]
        prev_el = points[start]
        if curr_el[0]>prev_el[1]: #capture all the non-overlapping points and increase the count 
            count+=1
            start=end
        end+=1
    return count
        