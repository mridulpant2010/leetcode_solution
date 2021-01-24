#https://leetcode.com/problems/pascals-triangle/

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
    row=[]
    for i in range(1,n+1):
        l = []
        for j in range(1,i+1):
            
            a=pascalTriangle(i,j,{})
            l.append(a)
            print(a)
        row.append(l)
    print(row)