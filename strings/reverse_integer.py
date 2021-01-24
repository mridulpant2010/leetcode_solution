
def reverse_integer(ax):
    if ax==0: return 0
    max_int = 2**31-1
    rev=0
    x=-ax if ax<0 else ax
    while x:
        re=x%10
        temp=rev*10+re
        if rev > (max_int - re) / 10:return 0
        rev=temp
        x=x//10
    return -temp if ax<0 else temp


if __name__=='__main__':
    a=reverse_integer(1534236469)
    print(a)
