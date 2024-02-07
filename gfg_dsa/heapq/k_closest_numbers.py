#https://github.com/mridulpant2010/grokking_coding_interview/blob/main/top_K_elements/'K'%20Closest%20Numbers%20(medium)%20-%20Grokking%20the%20Coding%20Interview_%20Patterns%20for%20Coding%20Questions.pdf

import heapq

#but we have to write the code for the nearest number to 
def binary_search(nums,pattern):
    start=0
    end=len(nums)-1
    while start<=end:
        mid = (start+end)//2#int(start+(end-start)/2)#(start+end)//2
        if (nums[mid]==pattern):
            return mid 
        if nums[mid]>pattern:
            end = mid-1
        else:
            start=mid+1
    if start>0:
        return start-1
    return start
        


def find_closest_number(nums,k,pattern):
    index = binary_search(nums,pattern)
    
    start = index-k
    end = index + k
    start = max(start,0)
    end = min(end,len(nums)-1)
    print(index,start,end)
    minheap=[]
    while start<=end:
        heapq.heappush(minheap,(abs(nums[start]-pattern),nums[start]))
        start+=1
    print(minheap)
    result= []
    for _ in range(k):
        ans =heapq.heappop(minheap)[1]
        result.append(ans)
    result.sort()
    return result 


arr = [1,1,1,10,10,10]; k = 1; x = 9
print(find_closest_number(arr,k,x))
print(find_closest_number([5,6,7,8,9],3,7))
# print(find_closest_number([2,4,5,6,9],3,6))
# print(find_closest_number([2,4,5,6,9],3,10))