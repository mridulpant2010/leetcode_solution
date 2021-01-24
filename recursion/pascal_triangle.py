
'''

recurrence relation for pascal triangle is given by the following 
f(i,j)=f(i−1,j−1)+f(i−1,j)
base condition is if j=1 then f(i,j)=1
'''

def pascalTriangle(i,j,d):
    if j==1 or i==j:
        return 1
    if (i,j) in d:
        return d[(i,j)]
    result= pascalTriangle(i-1,j-1,d)+pascalTriangle(i-1,j,d)
    d[(i,j)]=result
    
    return result
    
if __name__=='__main__':
    n=int(input())
    l=[]
    for i in range(1,n+2):
        row = [None for _ in range(n+1)]
        a=pascalTriangle(n+1,i,{})
        l.append(a)
        print(a)
    print(l)
    