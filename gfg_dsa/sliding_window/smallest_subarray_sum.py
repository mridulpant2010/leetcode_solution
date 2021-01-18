def smallest_subarray_with_given_sum(s, arr):
  i=0
  j=0
  sum_arr=0
  min_l=100
  while j<len(arr):
    sum_arr+=arr[j]
    while sum_arr>=s:
      g_len=j-i+1
      print(g_len,i,j)
      min_l=min(min_l,g_len)
      sum_arr-=arr[i]
      i+=1
    j+=1
  return min_l

from collections import defaultdict
def longest_substring_with_k_distinct(st, k):
    j=0
    i=0
    d=defaultdict(int)
    max_len=-1
    for el in st:
        d[el]+=1
    count=k
    while j<len(st):
        d[st[j]]-=1
        print(d,st[j])
        if len(d.keys())==k:
            if count==0:
                max_len=max(max_len,j-i+1)
            d[st[i]]+=1
            i+=1
        j+=1
    return max_len
            

if __name__=='__main__':
    
    arr=[2, 1, 5, 2, 8]
    s=7
    a=longest_substring_with_k_distinct('araaci', 2)
    print(a)
    

from collections import defaultdict
def countOccurence(arr,n,k):
    d=defaultdict(int)
    for el in arr:
        d[el]+=1
    c=n//k
    count=0
    for k,v in d.items():
        if v>c:
            count+=1
    return count
 