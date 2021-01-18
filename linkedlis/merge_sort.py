def merge(arr,start,mid,end):
    left=arr[start:mid+1]
    right=arr[mid+1:end+1]
    i=0
    j=0
    k=start
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]=right[j]
            k+=1
            j+=1            
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1
        
def merge_sort(arr,start,end):
    if start<end:
        mid=(start+end)//2
        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,start,mid,end)
    return arr

if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    merge_sort(arr,0,n)
    print(arr)