#question link:
#https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3518/

def maxPower(s):
    n_len=len(s)
    arr=[0]*n_len
    arr[n_len-1]=1
    i =len(s)-2
    while i>=0:
        if s[i]==s[i+1]:
            arr[i]=arr[i+1]+1
        else:
            arr[i]=1
        i-=1
    return max(arr)

print(maxPower("leetcode"))


def convertInt(num1):
    x=0
    if num1[0]=='-':
        num1=num1[1:]
        x=1
    ans=0
    a=1
    for i in range(len(num1)-1,-1,-1):
        sol =ord(num1[i])-ord('0')
        ans=ans+sol*a
        a=a*10
    if x==1: 
        return -ans
    else:
        return ans