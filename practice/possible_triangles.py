'''
question link: 

https://practice.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1/?track=DS-Python-Sorting&batchId=273


'''
import timeit

def findNumberOfTriangles(arr,n):
    arr.sort()
    c=0
    for i in range(n):
        for next in range(i+1,n):
            sum=arr[i]+arr[next]
            for j in range(next+1,n):
                if sum>arr[j]:
                    c+=1
    return c


def findTriangles(arr):
    arr.sort()
    n=len(arr)
    c=0
    for i in range(n-1,0,-1):
        l=0
        r=i-1
        while l<r:
            if arr[l]+arr[r]>arr[i]:
                c+=r-l
                r-=1
            else:
                l+=1
    return c
    

if __name__=='__main__':
    
    start=timeit.timeit()
    arr=[ 7,8,3,4,6,9]
    n=len(arr)
    c=findNumberOfTriangles(arr,n)
    end=timeit.timeit()
    print(c,end-start)
    
    s=timeit.timeit()
    d=findTriangles(arr)
    e=timeit.timeit()
    print(d,e-s)