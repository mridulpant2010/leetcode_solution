from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start=0
        end = len(nums)-2
        last = len(nums)-1
        hash_set = set()
        while start<end:
            target = -1* nums[start]
            next_n = start+1
            res=[]
            while next_n<last:
                curr_sum = nums[next_n]+ nums[last]
                if curr_sum==target:
                    res.append(nums[start])
                    res.append(nums[next_n])
                    res.append(nums[last])
                    res.sort()
                    if tuple(res) not in hash_set:
                        hash_set.add(tuple(res))
                    next_n+=1
                    last-=1
                if curr_sum>target:
                    last-=1
                else:
                    next_n+=1
            start+=1
        return list(hash_set)


if __name__=="__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    ans = s.threeSum(nums)
    print(ans)