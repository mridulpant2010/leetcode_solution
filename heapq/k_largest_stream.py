import heapq

class KthLargestNumberInStream:
    
    def __init__(self,nums,k):
        self.k=k
        self.minHeap=[]
        start=0
        while start<len(nums):
            heapq.heappush(self.minHeap,nums[start])
            if len(self.minHeap)>k:
                heapq.heappop(self.minHeap)
            start+=1
        
    def add(self,  num):
        heapq.heappush(self.minHeap,num)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
if __name__=='__main__':
    ans=KthLargestNumberInStream([3,1,5,12,2,11],4)
    print(ans)
    print(ans.add(6))
    print(ans.add(13))
    print(ans.add(4))