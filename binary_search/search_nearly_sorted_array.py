#https://www.geeksforgeeks.org/problems/search-in-an-almost-sorted-array/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

class Solution:
    def findTarget(self, arr, target):
        
        start= 0
        end = len(arr)-1
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==target :
                return mid
            elif mid-1>=start and target==arr[mid-1] :
                return mid-1
            elif mid+1<=end and target==arr[mid+1]:
                return mid+1
            elif arr[mid]<target:
                start=mid+2
            else:
                end=mid-2
        return -1
            