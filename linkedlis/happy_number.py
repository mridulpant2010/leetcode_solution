def find_square(digit):
    ans=0
    while digit:
        rem=digit%10
        ans+= rem**2
        digit=digit//10
    return ans 

def isHappy(digit):
    fast_pointer=digit
    slow_pointer=digit
    while fast_pointer!=1 and find_square(fast_pointer)!=1:
        fast_pointer = find_square(find_square(fast_pointer))
        slow_pointer = find_square(slow_pointer)
        if fast_pointer==slow_pointer:
            return False
    return True
            

if __name__ == '__main__':
    ans= find_square(12)
    print(isHappy(ans))
    #print(ans)