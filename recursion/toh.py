def toh(n,a,b,c):
    if n==1: 
        print("Move ring 1 from",a ,"to",c)
        return
    else:
        toh(n-1,a,c,b)
        print("Move ring ",n,"from ",a,"to",c)
        toh(n-1,b,a,c)

if __name__ == "__main__":
    n=int(input())
    toh(n,'A','B','C')