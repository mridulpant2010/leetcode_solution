def bs(num,target):
    start=1
    end=num
    while start<=end:
        mid = (start+end)//2
        #target = guess(mid)
        if target ==0:
            return mid

        elif target >0:
            start=mid+1
        else:
            end= mid-1


#binary search with the first occurrence
def bs_first_sequence(arr,target):
    start=0
    end = len(arr)
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            if (mid)!=0 and arr[mid] == arr[mid-1]:
                end=mid-1
            else:
                return mid
        elif arr[mid] >target:
            end = mid-1
        else:
            start = mid+1
    else:
        return -1
#binary search with the last occurrence

def bs_last_sequence(arr,target):
    start=0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            if mid!=len(arr)-1 and arr[mid]==arr[mid+1]:
                start=mid+1
            else:
                return mid
        elif arr[mid] < target:
            start=mid+1
        else:
            end = mid-1
    else:
        return -1


#template 2 for the binarySearch:
def binarySearch(nums,target):
    '''
    :type nums: List[int]
    :type target: int
    :rtype: int
    '''
    start=0
    end=len(nums)
    if len(nums)==0:
        return -1
    while start<end:
        mid = (start+end)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid
    #post-processing
    if start!=len(nums) and nums[start]==target:
        return start
    return -1


def isBadVersion(version):
    pass

def findfirstOccurrence(array,target):
    start=0
    end = len(array)-1
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            if mid!=0 and array[mid]==array[mid-1]:
                end=mid-1
            else:
                return mid
        elif array[mid] <target:
            start=mid+1
        else:
            end = mid-1
    return -1
            
            
#not the correct approach to solve this question
def firstBadVersion(n):
    l=[]
    for i in range(1,n+1):
        if isBadVersion(i)==False:
            l.append(0)
        else:
            l.append(1)
    


#finding the peak element using the binarySearch approach

#searching in a sorted-rotated array

def searchRotatedSortedArray(arr,target):
    #case1: mid-point is present in the first-half
    #case2: mid-point is present in the second-half
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        #it is also one of the interesting problem
        if arr[mid]==target:
            return mid
        elif arr[start]<=arr[mid]:
            if arr[mid]>=target and target>=arr[start]:
                end=mid-1
            else:
                start=mid+1
        else:
            if arr[mid]<=target and target<=arr[end]:
                start=mid+1
            else:
               end= mid-1
    else:
        return -1

def peakElement(arr, k):
    # Code here
    start=0
    end=k
    while start<end:
        mid=(start+end)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>=arr[start]:
            if arr[start] <=k and k<=arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if arr[mid]<=k and k<=arr[end]:
                start=mid+1
            else:
                end=mid-1
    return -1
#
def kthroot(num,kroot):
    start=0
    end =num
    ans= 0
    while start<=end:
        mid =(start+end)//2
        if mid**kroot >num:
            end=mid-1
        elif mid**kroot <num:
            ans=mid
            start=mid+1
        else:
            return mid
    return ans

#find the min-element in a sorted-rotated array

def binary_search(arr):
    start=0
    end=len(arr)-1
    n=len(arr)
    while start<=end:
        if arr[start]<=arr[end]:
            return start
        mid= (start+end)//2
        next=(mid+1)%n
        prev=(mid-1+n)%n
        print(arr[prev],arr[mid],arr[next])
        if arr[mid] <= arr[next] and arr[mid]<=arr[prev]:
            return mid
        if arr[start]>arr[mid]:
            end=mid-1
            
        else:
            start=mid+1
    return -1