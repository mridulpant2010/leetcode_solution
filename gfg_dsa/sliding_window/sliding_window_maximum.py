def maxSlidingWindow(self, nums: List[int], k: int):
    i=0
    j=0
    l=[]
    st=[]
    if k==1:
        return nums
    while j <len(nums):
        while len(st)>0 and st[-1]<nums[j]:
            st.pop()
        st.append(nums[j])
        if (j-i+1) < k:
            j+=1
        elif (j-i+1)==k:
            l.append(st[0])
            if st[0]==nums[i]:
                st.pop(0)
            i+=1
            j+=1
    return l

print(maxSlidingWindow([1,-1],1))