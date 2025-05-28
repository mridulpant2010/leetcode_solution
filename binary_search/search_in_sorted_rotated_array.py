class Solution:
    def binary_search(self,nums, target,start,end):
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
        return -1
    def search(self, nums, target: int) -> int:
        start=0 
        end=len(nums)-1
        n=len(nums)-1
        if n==0:
            return -1
        while start<=end:
            mid = (start+end)//2
            next_n = (mid+1)%n
            prev = (mid-1+n)%n
            print(mid,next_n,prev)
            if nums[mid]<=nums[next_n] and nums[mid]<=nums[prev]:
                break
            if nums[mid]>=nums[start]:
                start=mid
            elif nums[mid]<=nums[end]:
                end=mid-1
        print(mid)
        res1 = self.binary_search(nums,target,0,mid-1)
        res2 = self.binary_search(nums,target,mid,n)
        return max(res1,res2)
    
from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        n = len(nums)

        # Finding the pivot (smallest element)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:  # Pivot is in the right half
                start = mid + 1
            else:  # Pivot is in the left half
                end = mid

        pivot = start  # Pivot index

        # Perform binary search in both halves
        res1 = self.binary_search(nums, target, 0, pivot - 1)
        res2 = self.binary_search(nums, target, pivot, n - 1)

        return max(res1, res2)
    
if __name__=="__main__":
    s = Solution()
    nums=[4,5,6,7,0,1,2]; target=0
    res=s.search(nums,target)
    print(res)
    
    