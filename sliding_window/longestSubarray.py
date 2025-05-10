#https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

class Solution:
    def longestSubarray(self, arr, k):  
        index=0
        prefix_sum=0
        hash_map={0:-1}
        for el in range(len(arr)):
            prefix_sum+=arr[el]
            #prefix_arr[el]= prefix_arr[el-1]+arr[el]
            if prefix_sum-k in hash_map:
               index = max(index,el-hash_map[prefix_sum-k])
            if prefix_sum not in hash_map:
                hash_map[prefix_sum]=el
               #print(prefix_sum,index,arr[el])
        return index
            


if __name__ == "__main__":
    s = Solution()
    arr=[94, -33, -13 ,40, -82, 94, -33, -13, 40, -82]
    k= 52
    index=s.longestSubarray(arr,k)
    print(index)