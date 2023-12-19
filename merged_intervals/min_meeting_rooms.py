import heapq
def min_meeting_rooms(arr):
    he = []
    min_he = 0
    arr.sort(key=lambda x: x[0])
    for i in range(len(arr)) :
        curr_el = arr[i]
        while len(he)>0 and he[0][0]<=curr_el[0]:  #i am comparing if there are any non-overlapping intervals between the current_el and the heap 0 index element. and if yes remove all until the heap is empty or the overlapping intervals are found.
            heapq.heappop(he)
        heapq.heappush(he,(curr_el[1],curr_el[0])) #a small trick that is done is i am storing the end interval first and later the start interval.
        min_he = max(min_he,len(he))
    return  min_he


if __name__ == "__main__":
    array = [[1,4],[2,5],[7,9]]
    ans = min_meeting_rooms(array)
    print(ans)

    array = [[6,7],[2,4],[8,12]]
    ans = min_meeting_rooms(array)
    print(ans)


    array = [[4,5],[2,3],[2,4],[3,5]]
    ans = min_meeting_rooms(array)
    print(ans)