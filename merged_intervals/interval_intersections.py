
#https://leetcode.com/problems/interval-list-intersections/
def intervalIntersection(intervals1, intervals2):
    """ 
    :type firstList: List[List[int]]
    :type secondList: List[List[int]]
    :rtype: List[List[int]]
    """
    i=0
    j=0
    intersections=[]
    while i < len(intervals1) and j< len(intervals2):
        start = max(intervals1[i][0],intervals2[j][0])
        end = min(intervals1[i][1],intervals2[j][1])

        if start<=end:
            intersections.append([start,end])
        
        if intervals1[i][1] < intervals2[j][1]:
            i+=1
        else:
            j+=1
    return intersections