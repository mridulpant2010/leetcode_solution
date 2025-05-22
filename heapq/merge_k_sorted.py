import heapq

def merge(arr):
    # code here
    # return merged list
    heap=[]
    output=[]
    heapq.heapify(heap)
    for i in range(len(arr)):
        heapq.heappush(heap,(arr[i][0],(i,0)))
    while len(heap)>0:
        top = heapq.heappop(heap)
        output.append(top[0])
        i = top[1][0]
        j = top[1][1]
        if (j+1<len(arr[i])):
            heapq.heappush(heap,(arr[i][j+1],(i,j+1)))
    return output

def prepare_arr(ar):
    b=[]
    a=[]
    c=0
    while c<len(ar):
        d=0
        a=[]
        while d<k:
            a.append(ar[c+d])
            d+=1
        b.append(a)
        c+=k
    return b

if __name__=='__main__':
    k,n=list(map(int,input().split()))
    arr= list(map(int,input().split()))
    ar= prepare_arr(arr)
    print(ar)
    output=merge(ar)
    print(*output)
