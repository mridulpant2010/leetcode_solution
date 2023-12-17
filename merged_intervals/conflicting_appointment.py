

def conflicting_appointments(arr):
    """
    :type arr: List[List[int]]
    :rtype: int
    """
    arr.sort(key=lambda x: x[0])
    prev_el = arr[0]
    for i in range(1,len(arr)):
        curr_el = arr[i]
        if curr_el[0] <= prev_el[1]:
            return False
        else:
            prev_el = curr_el
    return True

if __name__ == '__main__':
    arr =[[4,5],[2,3],[3,6]]
    ans = conflicting_appointments(arr)
    print(ans)
    arr2 = [[1,4],[2,5],[7,9]]
    ans2 = conflicting_appointments(arr2)
    print(ans2) 
    arr3 = [[6,7],[2,4],[8,12]]
    ans3 = conflicting_appointments(arr3)
    print(ans3) 