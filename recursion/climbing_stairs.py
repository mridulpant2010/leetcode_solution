#using memoization
import timeit

def climbStairs_memo(n,d):
    if n==1 or n==2:
        return n
    if n in d:
        return d[n]
    a= climbStairs_memo(n-1,d)+climbStairs_memo(n-2,d)
    d[n]=a
    return a

def climbStairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return climbStairs(n-1)+climbStairs(n-2)

st=timeit.timeit()
a=climbStairs(6)
en=timeit.timeit()
print(en-st)
print(a)

b=climbStairs_memo(6,{})
print(b)