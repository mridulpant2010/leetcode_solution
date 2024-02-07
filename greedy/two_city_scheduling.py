#https://leetcode.com/problems/two-city-scheduling/submissions/1123427425/
def twoCitySchedCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    costs.sort(key=lambda x:x[0]-x[1])
    total_cost=0
    start=0
    end= len(costs)-1
    while start <= end:
        total_cost+=costs[start][0]+costs[end][1]
        start+=1
        end-=1
    return total_cost