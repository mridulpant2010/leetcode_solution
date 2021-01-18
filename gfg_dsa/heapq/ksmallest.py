import heapq
#heapq by default prepares the max-heap
#k-smallest --> prepare a max-heap
#k-largest --> prepare a min-heap
def ksmallest(arr,k):
    #creating a empty heap in python 
    he=[]
    heapq.heapify(he)
    
    for i in range(len(arr)):
        heapq.heappush(he,-1*arr[i])
        if len(he)>k:
            heapq.heappop(he)
    print(he)
    return -1*heapq.heappop(he)   



def klargest(arr,k):
    #for k largest we have to build  a min-heap
    he=[]
    heapq.heapify(he)
    
    