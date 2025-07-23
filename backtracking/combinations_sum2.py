class Solution:
    def combinations(self,nums,path,result,curr_sum,target):
        if curr_sum == target:
            result.append(path.copy())
            return
        h_set = set()
        if curr_sum < target:
            for i in range(len(nums)):
                if nums[i] not in h_set:
                    h_set.add(nums[i])
                    curr_sum += nums[i]
                    path.append(nums[i])
                    self.combinations(nums[i:],path,result,curr_sum,target)
                    curr_sum-=nums[i]
                    path.pop()
            

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.combinations(candidates,[],result,0,target)
        return result

        