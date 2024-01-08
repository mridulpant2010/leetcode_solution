from itertools import combinations
from collections import defaultdict
def countBadPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = defaultdict(list)
    total_pairs = len(list(combinations(range(len(nums)), 2)))
    counter=0
    for i in range(len(nums)):
        d[nums[i]-i].append(i)
    max_len = 0
    for _,v in d.items():
        max_len = max(max_len,len(v))
    print(max_len)/2
    return total_pairs-max_len         

if __name__ == "__main__":
    nums = [4,1,3,3]
    ans=countBadPairs(nums)
    print(ans)