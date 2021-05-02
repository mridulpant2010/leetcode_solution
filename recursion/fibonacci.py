#https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/
import timeit

def fibo(n,d):
    if n<2:
        return n
    if n in d:
        print(d[n])
        return d[n]
    result= fibo(n-1,d)+fibo(n-2,d)
    return result


def fibo1(n):    
    if n<2:
        return n    
    return fibo1(n-1)+fibo1(n-2)
    

if __name__=='__main__':
    n=int(input())
    a1=fibo(n,{})
    print(a1)
