def knapsack(wt,val,w,n):
    
    #base-case 
    if w==0 or n==0:
        return 0
    inc=-1
    ans=-1
    exc=-1    
    
    #recursive-case
    if wt[n-1]<=w:
        inc = val[n-1] + knapsack(wt,val,w-wt[n-1],n-1)
    exc = knapsack(wt,val,w,n-1)
    ans = max(inc,exc)
    return ans


if __name__ == "__main__":
    wt=[1,2,3,5]
    val=[40,20,30,100]
    
    ans = knapsack(wt,val,7,4)
    print(ans)