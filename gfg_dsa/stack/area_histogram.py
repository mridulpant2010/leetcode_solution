#writing a function for calculating area_histogram question solution
def nearest_smaller_right(arr):
    st=[]
    new_arr=[]
    n_len=len(arr)
    for i in range(n_len-1,-1,-1):
        if i==n_len-1:
            new_arr.append(n_len)
        elif len(st)>0 and arr[st[-1]]<=arr[i]:
            new_arr.append(st[-1])
        elif len(st)>0 and arr[st[-1]]>arr[i]:
            while len(st)>0 and arr[st[-1]]>arr[i]:
                st.pop()
            new_arr.append(n_len) if len(st)==0 else new_arr.append(st[-1])
        st.append(i)
    new_arr.reverse()
    print(new_arr)
    return new_arr
    
def nearest_smaller_left(arr):
    st=[]
    new_arr=[]
    for i in range(len(arr)):
        if i==0:
            new_arr.append(-1)
        elif len(st)>0 and arr[st[-1]]<arr[i]:
            new_arr.append(st[-1])
        elif len(st)>0 and arr[st[-1]]>=arr[i]:
            while len(st)>0 and arr[st[-1]]>=arr[i]:
                st.pop()
            new_arr.append(-1) if len(st)==0 else new_arr.append(st[-1])
        st.append(i)
    print(new_arr)
    return new_arr

def area_histogram(arr):
    width_arr=[]
    max_area=0
    left = nearest_smaller_left(arr)
    right=nearest_smaller_right(arr)
    for i in range(len(arr)):
        width_arr.append(right[i]-left[i]-1)
    print(arr)
    print(width_arr)
    for i in range(len(arr)):
        max_area= max(max_area,arr[i]*width_arr[i])
    return max_area


if __name__ == '__main__':
    
    #n = int(input())
    #arr=list(map(int,input().split()))
    print(area_histogram([2,1,5,6,2,3]))