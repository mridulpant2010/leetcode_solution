#
'''
properties of binary representation is that they have only one bit set in their binary representation
which mean x and x-1 will be zero.

2i as 1 << i

tricks with the binary representation
1-  x ^ ( x & (x-1)) : Returns the rightmost 1 in binary representation of x
2-  x & (-x) : Returns the rightmost 1 in binary representation of x
3-  x | (1 << n) : Returns the number x with the nth bit set.
'''

def isPowerofTwo(x):
    return (x&(x-1))

def count_one(n):
 count=0
 while n:
  n = n&(n-1)
  count+=1
 return count


#how to find the power(a,b) in logn times using the bitmasking approach


def xor2values():
    pass

#find all the subset of a set 
def findSubset(a,n):
    outer=[]
    for i in range(0,(1<<n)):
        inner=[]
        for j in range(0,n):
            if i & (1<<j):
                #print(a[j],end=' ')
                inner.append(a[j])
        #print()
        outer.append(inner)
    print(outer)
        
#difference b/w default dict and dict

def xorOperation(n,start):
    xor_list=list(range(start,start+2*n,2))
    a = 0
    for el in xor_list:
        a^=el
    return a    


if __name__=='__main__':
    t= int(input())
    while t!=0:
        a,b = list(map(int,input().split()))
        count=0
        for i in range(a,b+1):
            count+=count_one(i)
        print(count)
        t-=1