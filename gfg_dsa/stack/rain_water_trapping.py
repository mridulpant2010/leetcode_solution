def rain_water_trapping(arr):
    '''
    time-complexity here is O(n^2)
    '''
    width_arr=[]
    for i in range(len(arr)-1):
        right_max=max(arr[i+1:])
        left_max=max(arr[0:i+1])
        ans=min(right_max,left_max)
        res=ans-arr[i]
        if res >=0:
            width_arr.append(res)
    print(width_arr)
    #width_arr.append(left_max)
    print(sum(width_arr))


def rainWaterTrapping(arr):
    width_arr = []
    n_len=len(arr)
    left_arr=[0]*n_len
    right_arr=[0]*n_len
    left_arr[0]=arr[0]
    right_arr[n_len-1]=arr[n_len-1]
    for i in range(1,n_len):
        left_arr=max(left_arr[i-1],arr[i])
    for i in range(n_len-2,-1,-1):
        right_arr[i]=max(right_arr[i+1],arr[i])
    for i in range(n_len):
        ans= min(left_arr[i],right_arr[i])-arr[i]
        width_arr.append(ans)
    print(sum(width_arr))
            

if __name__=='__main__':
    n = int(input())
    arr=list(map(int,input().split()))
    rain_water_trapping(arr)