#write  a tail-recursive function of factorial

def fact(n):
    if n==0: return 1
    return n*fact(n-1)

def fact(n,op=1):
    if n<1: return op
    return fact(n-1,n*op)

def isPalindrome(str2):
    start=0
    end=len(str2)-1
    while start<=end:
        if str2[start]!=str2[end]:
            return False
        start+=1
        end-=1
    return True

str2='aaabaa'
e=len(str2)-1
def isPalindrome(str2,start,end):
    if start>=end:
        return True
    
    if str2[start]!=str2[end]:
        return False
    return isPalindrome(str2,start+1,end-1)


def digit_sum(n):
    sum=0
    while n>0:
        a=n%10
        sum+=a
        n=n//10
    return sum