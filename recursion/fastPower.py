def power(a,n):
    if n==0:
        return 1
    return a*power(a,n-1)



def fastPower2(a,n):
    if n==0:
        return 1
    if n%2==0:
        return fastPower2(a,n//2)**2
    else:
        return  a*fastPower2(a,n//2)**2
    
def fastPower(a,n):
    
    '''
    solution from prateek bhaiya
    '''
    if n==0:
        return 1
    ans=fastPower(a,n//2)
    ans=ans*ans
    if n&1:
        return ans*a
    return ans
    
ans=power(2,10)
b=fastPower2(2,10)
print(b)
#print(ans)