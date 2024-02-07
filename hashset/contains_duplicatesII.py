def containsNearbyDuplicate(arr, k):
    s = set()
    start=0
    end=0
    while end < len(arr):
        print(s,start,end)
        if arr[end] not in s:
            s.add(arr[end])
        else:
            print(start,end)
            while end-start>k:
                if arr[start] in s and end-start <= k:
                        return True
                s.remove(arr[start])
                start+=1    
            else:
                start+=1
        end+=1
    return False

if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 1
    print(containsNearbyDuplicate(nums, k))
    print(containsNearbyDuplicate([1,2,3,1], 3))
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))