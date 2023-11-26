def find_greatest(gas,cost):
    k = len(gas)
    max_so_far = 0
    next_greatest=-1
    diff = []
    for i in range(k):
        diff.append(gas[i] - cost[i])
        max_so_far += diff[i]
        if max_so_far < 0:
            next_greatest = i+1
            max_so_far=0
    if sum(diff) >=0:
        return next_greatest                          
    else:
        return -1
    
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
find_greatest(gas,cost)