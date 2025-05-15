class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-2
        goal = i+1
        while i>=0:
            if nums[i]+i >= goal:
                goal=i
            i-=1
        return goal==0



#https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
def canJump(arr):
    """
    :type nums: List[int]
    :rtype: bool
    """
    target= len(arr)-1
    end = len(arr)-1
    start=0
    while end>=start:
        if end+arr[end]>=target:
            target=end
        if target==start:
            return True
        end-=1
    return False

if __name__ == "__main__":
    arr = [2,3,1,1,4]
    ans = canJump(arr)
    print(ans)

    arr = [3,2,1,0,4]
    ans = canJump(arr)
    print(ans)

    arr = [2,3,0,1]
    ans = canJump(arr)
    print(ans)

    arr = [0]
    ans = canJump(arr)
    print(ans)