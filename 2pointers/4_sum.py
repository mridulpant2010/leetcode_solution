from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                sum_v =  nums[i]+nums[j]
                d[sum_v].append((i,j))
        possible_pairs=set()
        for k, v in d.items():
            if target-k in d:
                for values in d[k]:
                    for el in d[target-k]:
                        indices= {values[0],values[1],el[0],el[1]}
                        if len(indices)==4 :
                            res = sorted([nums[values[0]],nums[values[1]],nums[el[0]],nums[el[1]]])
                            possible_pairs.add(tuple(res))
        return list(possible_pairs)

s = Solution()
nums=[1,0,-1,0,-2,2]
target=0
ans = s.fourSum(nums,target)
print(ans)