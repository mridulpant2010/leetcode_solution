#https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/

def minOperations(nums,x):
    total=sum(nums)
    target=total-x
    if target<0: 
        return -1
    if target==0:
        return len(nums)
    
    i=0
    j=0
    max_sum=0
    max_len=-1
    curr_sum=0
    while j<len(nums):
        curr_sum+=nums[j]
        while curr_sum>target:
            curr_sum-=nums[i]
            i+=1
        #if curr_sum==target:
        max_len=max(max_len,j-i+1)
        j+=1
    #print(max_len)
    return max_len if max_len==-1 else len(nums)-max_len


if __name__=='__main__':
    nums = [1,1,4,2,3] 
    x = 5
    ans=minOperations(nums,x)
    print(ans)