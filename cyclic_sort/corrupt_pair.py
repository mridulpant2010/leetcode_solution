
def find_corrupt_numbers(nums):
    current_position=0
    ans=[]
    while current_position<len(nums):
        correct_position=nums[current_position]-1
        if nums[current_position]!=nums[correct_position]:
            nums[current_position],nums[correct_position] = nums[correct_position],nums[current_position]
        else:
            current_position += 1
    
    for i in range(len(nums)):
        if nums[i]!=i+1:
            ans.append([nums[i],i+1])
    return ans


if __name__=='__main__':
    nums = [3,1,2,5,2]
    ans = find_corrupt_numbers(nums)
    print(ans)
    