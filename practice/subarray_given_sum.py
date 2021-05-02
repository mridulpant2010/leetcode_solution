#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1/?track=SPC-Searching&batchId=135#

def subarraySum(arr,n,target_sum):
    i=0
    curr_sum=0
    j=0
    while i<n:
        curr_sum+=arr[i]
        
        while curr_sum>target_sum:
            curr_sum-=arr[j]
            j+=1
        if curr_sum==target_sum:
            print (j+1,i+1)
            break
        i+=1
    else:
        print(-1)
        
import math
def main():
        T=int(input())
        while(T>0):
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            A=list(map(int,input().split()))
            subarraySum(A, N, S)
            
            print()
            
            T-=1
if __name__ == "__main__":
    main()    
    

def fun(n):
    if n==0: return 
    print(n)
    fun(n-1)
    
def fun(n,i=1):
    if n<1: return 
    print(i)
    fun(n-1,i+1)