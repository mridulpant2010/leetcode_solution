
def find_missing_positive_number(nums):
    start_position = 0
    ans=[]
    while  start_position < len(nums):
        current_position = nums[start_position]-1
        if nums[start_position] >0  and nums[current_position]!=nums[start_position]:
            nums[current_position],nums[start_position] = nums[start_position],nums[current_position]
        else:      
            start_position +=1
    for i in range(len(nums)):
        if nums[i]!=i+1:
            return i+1
    return len(nums)+1

if __name__ == '__main__':
    #nums = [-3,1,5,4,2]
    #nums = [3,-2,0,1,2]
    nums = [3,2,5,1]
    result = find_missing_positive_number(nums)
    print(result)