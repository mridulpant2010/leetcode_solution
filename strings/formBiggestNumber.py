from functools import cmp_to_key
def compare(a,b):
    print(a+b,"",b+a,( a+b> b+a))
    return a+b> b+a
def formBiggestNumber(ar):
    #ans=sorted(ar,key=cmp_to_key(compare))
    ar.sort(key=cmp_to_key(compare))
    print(ar)
    #return ''.join(ans)

if __name__ == '__main__':
    t=int(input())
    while t:
        n=int(input())
        #ar =list(map(int,input().split()))
        ar= input().split()
        an = formBiggestNumber(ar)
        print(an)
        t-=1