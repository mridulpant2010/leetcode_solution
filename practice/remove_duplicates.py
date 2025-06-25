def remove_duplicates(arr):
    end=len(arr)-1
    start=end
    while start>0 and end >1:
        if arr[end]==arr[start]:
            start-=1
            arr[end-1]=arr[start]
        else:
            start-=1
            end-=1
    return arr[end:]

if __name__=="__main__":
    arr=[1,2,2,3,4,4,5]
    res=remove_duplicates(arr)
    print(res)