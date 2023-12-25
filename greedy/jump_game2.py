
#https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
def jump_game2(nums):
    farthest_jump=0
    current_jump=0
    jumps=0
    for i in range(len(nums)-1):
        farthest_jump = max(farthest_jump,i+nums[i])
        print(i,farthest_jump)
        if i == current_jump:
            jumps+=1
            current_jump=farthest_jump
    return jumps

if __name__ == '__main__':
    nums=[2,3,1,1,4]
    ans=jump_game2(nums)
    print(ans)