def next_greater_left(ar):
    new_ar=[]
    st=[]
    for i in range(len(ar)-1,-1,-1):
        if i ==len(ar)-1:
            new_ar.append(-1)
        elif len(st)>0and st[-1]> ar[i]:
            new_ar.append(st[-1])
        elif len(st)>0 and st[-1]<=ar[i]:
            while len(st)>0 and st[-1]<=ar[i]:
                st.pop()
            new_ar.append(-1) if len(st)==0 else new_ar.append(st[-1])
        st.append(ar[i])
    new_ar.reverse()
    return new_ar
    #return dict(zip(ar,new_ar))



if __name__=='__main__':
    n = int(input())
    st=list(map(int,input().split()))
    output= next_greater_left(st)
    print(*output)
    
    

def findFloor(arr,N,X):
    #Your code here
    low=0
    high=N-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==X:
            return mid
        elif arr[mid]<X:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans

def countOccurence(arr,n,k):
    a = [0]*11
    for el in arr:
        a[el]+=1
    print(a)
    an=n//k
    i=0
    count=0
    while i<len(a):
        if a[i]>an:
            count+=1
        i+=1
    return count


def floorSqrt(x): 
    low=0
    high=x
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if mid*mid<=x:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans

from collections import defaultdict
def isIsomorphic(s, t):
    d=defaultdict(str)
    for i in range(len(s)):
        if s[i] in d.keys():
            if t[i] != d[s[i]]:
                return False
        if s[i] not in d.keys() and t[i] in d.values():
            return False
        d[s[i]]=t[i]
    return len(d.keys())==len(d.values())

def findRestraunt(list1,list2):
    a_set=set(list1)
    b_set=set(list2)
    return a_set.intersection(b_set)

def reverse(x):
    a=1
    output=0
    while x:
        rem=x%10
        s=rem*a
        output+=s
        a=a*10
        x=x//10
    return output

def inputArray(r,c):
    matrix=[]
    for _ in range(r):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix

def searchMatrix(mat,k):
    r_num=len(mat)
    c_num=len(mat[0])
    i=r_num-1
    j=0
    while i>=0 and i <r_num and j>=0 and j <c_num:
        if mat[i][j]==k:
            return 1
        elif mat[i][j]>k:
            i-=1
        elif mat[i][j]<k:
            j+=1
    return 0

if  __name__=='__main__':
    r,c=list(map(int,input().split()))
    arr= inputArray(r,c)
    search=int(input())
    searchMatrix(arr,search)
    
    
def smallest_subarray_with_given_sum(s, arr):
  i=0
  j=0
  sum_arr=0
  min_l=100
  while j<len(arr):
    sum_arr+=arr[j]
    if sum_arr<s:
        j+=1 
    elif sum_arr>=s:
      g_len=j-i+1
      print(g_len,i,j)
      min_l=min(min_l,g_len)
      sum_arr-=arr[i]
      i+=1
      j+=1
  return min_l