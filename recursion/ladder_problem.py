def f(n,k):
    if n==0: return 0
    if n<0: return 0
    ans=0
    for i in range(1,k+1):
        ans+=f(n-i,k)
    return ans

if __name__ == '__main__':
    pass
