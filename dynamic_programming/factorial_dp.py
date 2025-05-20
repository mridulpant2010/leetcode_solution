def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def fact_dp(n):
    if n==0:
        return
    if t[n]!=-1:
        return t[n]
    t[n] = n*fact(n-1)
    return t[n]

if __name__=="__main__":
    #res=fact(10)
    n=10
    t=[-1 for i in range(n+1)]
    res=fact_dp(n)
    print(res)