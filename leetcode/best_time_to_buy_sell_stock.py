def bestTimeBuySellStock(arr):
    n_len=len(arr)
    ans_i=[]
    right_arr=[0]*n_len
    right_arr[n_len-1]=arr[n_len-1]
    for i in range(n_len-2,-1,-1):
        right_arr[i]=max(right_arr[i+1],arr[i])
    
    for i in range(n_len):
        ans_i.append(right_arr[i]-arr[i])
    print(ans_i)
    return max(ans_i)      


from collections import defaultdict
def sortByFreq(a,n):
    #code here
    d=defaultdict(int)
    for el in a:
        d[el]+=1
    d=tuple(d.items())
    #d=sorted(d,key=lambda x:x[0])
    d=sorted(d,key=lambda x:x[1],reverse=True)
    e=[el[0] for el in d]
    return e