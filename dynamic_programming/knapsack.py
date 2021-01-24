def knapsack(wt,val,w,n):
    #base-condition
    if w==0 or n==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    if wt[n-1]<=w:
        t[n][w]=max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
        return t[n][w]
    else:
        t[n][w]=knapsack(wt,val,w,n-1)
        return t[n][w]
    
def knapsack_topdown(wt,val,w,n,t):
    for i in range(n):
        for j in range(w):
            if i==0 or j==0:
                t[i][j]=0
    
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1]<=j:
                t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[n][w]=t[i-1][j]
    
    return t[n][w]


if __name__ == '__main__':
    
    n,w=list(map(int,input().split()))
    wt=list(map(int,input().split()))
    #[1 ,2 ,3 ,2 ,2 ]
    val=list(map(int,input().split()))
    #[8 ,4 ,0 ,5 ,3]
    rows, cols = (1001, 1001) 
    t  = [[0 for x in range(w + 1)] for x in range(n + 1)]
    #a=knapsack(wt,val,w,n)
    b=knapsack_topdown(wt,val,w,n,t)
    print(b)
    
        