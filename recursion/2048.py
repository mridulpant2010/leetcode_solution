def find_2048(n):
    while n:
        i=n%10
        n=n//10
        print(d[i],end=' ')
    
def find_n(n,d):
    if not n:
        return 
    i =n%10
    find_n(n//10,d)
    print(d[i],end=' ')

if __name__ == '__main__':
    d={
        1:'one',2:'two',3:'three',4:'four',
        5:'five',6:'six',7:'seven',8:'eight',9:'nine',
        0:'zero'
    }
    find_n(2048,d)
    