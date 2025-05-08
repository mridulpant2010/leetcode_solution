
# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        start=0
        end = len(arr)-1
        max_element=-1
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                start=mid+1
                max_element=max(max_element,mid)
            else:
                end=mid-1 
        return max_element
    
    
    
    def findCeil(self,arr,k):
        start=0
        end=len(arr)-1
        min_element=-1
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==k:
                min_element=arr[mid]
                return arr[mid]
            
            elif arr[mid] > k:
                end=mid-1
                min_element = min(min_element,arr[mid])
            else:
                start=mid+1
        return min_element
    

