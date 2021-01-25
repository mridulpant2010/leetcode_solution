def kthsymbol(n,k):
    if n==1 and k==1:
        return 0
    mid = 2**(n-1)/2
    if k<=mid:
        return kthsymbol(n-1,k)
    else:
        return not kthsymbol(n-1,k-mid)
    

if __name__ == '__main__':
    n=2
    k=1
    a=kthsymbol(n,k)
    print(int(a))