def merge_sort(arr,l,r):
    if l<r:
        m=(l+r)//2
        print(arr,l,m)
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)
        
def merge(arr, l, m, r): 
    # code here
    left=arr[l:m+1]
    right=arr[m+1:r+1]
    i=0
    j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            #output.append(arr[i])
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            k+=1
            j+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1
    

if __name__=='__main__':
    arr=[10 ,9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1]
    #arr=[10, 15, 20, 40, 8, 11, 55]
    o=merge_sort(arr,0,len(arr))
    print(arr)
    
from collections import defaultdict
def nonrepeatingCharacter(s):
    #code here
    d=[0]*26
    for el in s :
        d[ord(el)-ord('a')]+=1
    print(d)
    for o in range(len(d)):
        if d[o]==1:
            return chr(o+ord('a'))
    else:
        return '$'
    
    
def findDuplicate(nums) :
    j=0
    while j<len(nums):
        if j+1==nums[j]:
            j+=1
        else:
            nums[j],nums[nums[j]-1]=nums[nums[j]-1],nums[j]    
    for i in range(len(nums)):
        if i+1!=nums[i]:
            return i

import copy
def merge(nums1, m, nums2, n) :
    """
    Do not return anything, modify nums1 in-place instead.
    """
    left=copy.deepcopy(nums1)
    i=0
    j=0
    k=0
    while i<m and j<n:
        print(i,left[i],j,nums2[j],k,nums1[k])
        if left[i]<=nums2[j]:
            nums1[k]=left[i]
            #output.append(left[i])
            k+=1
            i+=1
            #print("if",nums1)
        else:
            nums1[k]=nums2[j]
            k+=1
            j+=1
    while i <m:
        print(i,left[i],j,nums2[j],k,nums1[k])
        nums1[k]=left[i]
        k+=1
        i+=1
    #print(nums1)
    while j<n:
        #output.append(nums2[j])
        print(i,left[i],j,nums2[j],k,nums1[k])
        nums1[k]=nums2[j]
        k+=1
        j+=1
    print(nums1)


def nonrepeatingCharacter(s):
    #code here
    d=defaultdict(int)
    for el in s:
        d[el]+=1
    for k,v in d.items():
        if v==1:
            return k
    else:
        return '$'