#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150

import heapq
def kSmallestPairs(nums1,nums2,k):
    final=[]
    he=[]
    heapq.heapify(he)
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            sum = nums1[i] + nums2[j]
            #print(sum,(nums1[i] , nums2[j]))
            heapq.heappush(he,(sum,[nums1[i] , nums2[j]]))
    start=0
    while start<k and len(he)>0:
        ans=heapq.heappop(he)
        final.append(ans[1])
        start+=1
    return final
    
if __name__ == '__main__':
    nums1= [1,1,2]#[1,7,11]
    nums2= [1,2,3]#[2,4,6]
    kSmallestPairs(nums1,nums2,2)
    