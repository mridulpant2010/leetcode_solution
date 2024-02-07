#https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

def nextLargerElement(arr,n):
    res=[-1]
    st= []
    st.append(arr[-1])
    for i in range(len(arr)-2,-1,-1):
        if arr[i]<st[-1]:
            res.append(st[-1])
        elif arr[i]>=st[-1]:
            while len(st)>0 and st[-1]<=arr[i]:
                st.pop()
            if len(st)==0:
                res.append(-1)
            else:
                res.append(st[-1])
        st.append(arr[i])
    new_lst = res[::-1]
    return new_lst
        
        