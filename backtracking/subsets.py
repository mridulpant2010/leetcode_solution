class Solution:
    def __init__(self):
        self.result=[]
        
    def subset_helper(self,nums, op):
        if len(nums)==0:
            self.result.append(op)
            return
        op1=op
        op2=op
        #op2.append(nums[0])
        #print(nums.pop(0))
        self.subset_helper(nums[1:],op1)
        self.subset_helper(nums[1:],op2+[nums[0]])

    def subsets(self, nums):
        self.subset_helper(nums,[])
        return self.result
    
if __name__ == "__main__":
    nums=[1,2,3]
    sol = Solution()
    ans=sol.subsets(nums)
    print(ans)
    