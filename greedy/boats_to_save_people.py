# https://leetcode.com/problems/boats-to-save-people/description/

def boats_to_save_people(nums,limit):
    nums.sort()
    boat_count=0
    left=0; right=len(nums)-1
    while left<=right:
        nums_sum=nums[left]+nums[right]
        if nums_sum<=limit:
            left+=1
            right-=1
        else:
            right-=1
        boat_count+=1
    return boat_count