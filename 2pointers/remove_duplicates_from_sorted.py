# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         correct_pos=1
#         len_ar = len(nums)
#         count=1
#         for current_pos in range(1,len_ar):
#             prev = current_pos-1
#             if nums[prev]!=nums[current_pos]:
#                 if count>1:
#                     correct_pos+=1
#                 nums[correct_pos] = nums[current_pos]
#                 correct_pos+=1
#             count+=1
        
#         if count>1:
#             nums[correct_pos] = nums[len_ar-1]
#             correct_pos+=1
            
#         return correct_pos

def removeDuplicates(nums):
    start=0
    end=2
    while end <len(nums):
        if nums[start]!=nums[end]:
            start+=2
            nums[start]=nums[end]
        end+=1
    print(nums[:start+1])
    

removeDuplicates([0,0,1,1,1,1,2,3,3])