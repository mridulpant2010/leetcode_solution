
#https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
def summary_ranges(nums):
    output=[]
    start=0
    end=1
    
    while end<len(nums):
        if nums[end]-nums[end-1] > 1:
            if nums[start] == nums[end-1]:
                output.append(str(nums[start]))
            else:
                output.append(str(nums[start])+"->"+str(nums[end-1]))
            start=end  
        end+=1
    
    if nums[start] == nums[end-1]:
        output.append(str(nums[start]))
    else:
        output.append(str(nums[start])+"->"+str(nums[end-1]))
    return output
    
if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    ans= summary_ranges(nums)
    print(ans) 
    nums2 = [0,2,3,4,6,8,9]
    ans2= summary_ranges(nums2)
    print(ans2)