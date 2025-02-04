def firstOccurrence(nums,target):
    start = 0
    end = len(nums)-1
    ans=-1
    while start <= end:
        mid = (start+end)//2
        print(nums[mid])
        if nums[mid] == target:
            if  nums[mid]==nums[mid-1]:
                end=mid-1
            else:
                ans= mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return ans


if __name__=="__main__":
    nums=[5,7,7,8,8,10]
    target=8
    ans = firstOccurrence(nums,target)
    print(ans)