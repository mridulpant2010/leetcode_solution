def partition(arr,l,h):
    i=l-1
    pivot=arr[h]
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
        

def quicksort(arr,low,end):
    if low<end:
        p=partition(arr,low,end)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,end)
    return arr

if __name__ == '__main__':
    l = list(map(int,input().split()))
    arr=quicksort(l,0,len(l)-1)
    print(arr)
