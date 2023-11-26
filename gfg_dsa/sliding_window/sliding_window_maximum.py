def maxSlidingWindow(self, nums: List[int], k: int):
    i=0
    j=0
    l=[]
    q=[]
    if k==1:
        return nums
    while j <len(nums):
        while len(q)>0 and q[-1]<nums[j]:
            q.pop()
        q.append(nums[j])
        if (j-i+1) < k:
            j+=1
        elif (j-i+1)==k:
            l.append(q[0])
            if q[0]==nums[i]:
                q.pop(0)
            i+=1
            j+=1
    return l

print(maxSlidingWindow([1,-1],1))