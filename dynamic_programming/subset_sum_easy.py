def subset_sum(wt,sum_e,n):
    for i in range(n+1):
        dp[i][0]=True
    
    for j in range(1,sum_e+1):
        dp[0][i]=False
    
    for i in range(1,n+1):
        for j in range(1,sum_e+1):
            if wt[i-1]<=j:
                dp[i][j]=(dp[i-1][j-wt[i-1]] or dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp)
    return dp[n][sum_e]
                    


if __name__ == '__main__':
    t=int(input())
    while t:
        n=int(input())
        wt=list(map(int,input().split()))
        sum_e=0
        print(wt)
        dp  = [[False for x in range(sum_e + 1)] for x in range(n + 1)]
        ans=subset_sum(wt,sum_e,n)
        if ans:
            print("Yes")
        else:
            print("No")
        t-=1

