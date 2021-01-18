def targetSumPair(element_list,n,target):
    num_dict={}
    for num in range(n):
        diff=target-num
        num_dict[num]=diff
    return num_dict

def findithdigit(elem):
    while elem//10:
        elem=elem//10
    return elem

def formBiggestNumber(element_list):
    biggest_dict={}
    for elem in element_list:
        biggest_dict[elem]=findithdigit(elem)
    print(biggest_dict)
    res=sorted(biggest_dict.items(),key=lambda x:x[1],reverse=True)
    res_final=[str(el[0]) for el in res]
    print(res_final)
    st= ''+res_final[0]
    st+= ''.join(res_final[-1:0:-1])
    return st

def sanketString(k,strn):
    d=dict()
    for i in strn:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    res= sorted(d.items(),key=lambda x:x[1])
    dif=k-res[0][1]
    max_perfectness=res[1][1]+dif
    print(max_perfectness)



def maximumSumCircularSubarray(arr_elements):
    
    
    #case1 
    curr_sum=0
    max_far=0
    for i in range(len(arr_elements)):
        curr_sum+=arr_elements[i]
        if curr_sum<0:
            curr_sum=0
            
        if max_far<curr_sum:
            max_far=curr_sum
    
    
    #case2 -for circular subarray
    arr_elements=list(map(lambda x:x*(-1),arr_elements))
    arr_sum=sum(arr_elements)
    current_sum=0
    max_so_far=0
    i=0
    while i<len(arr_elements):
        current_sum+=arr_elements[i]
        if current_sum>max_so_far:
            max_so_far=current_sum
        if current_sum <0:
            current_sum=0
        i+=1
    #print(max_so_far)
    print(max(-(arr_sum-max_so_far),max_far))
    
    
def isMonotonic(A):
    i=1
    n=len(A)
    while i<n and A[i-1]<=A[i]:
        i+=1
    
    j=1
    while j<n and A[j-1]>=A[j]:
        j+=1
    return j==n or i==n

def maxLengthBitonic(size,arr_elements):
    #initializing the 2 arrays
    inc = [1]*size
    dec= [1]*size
    #construct an increasing sequence array
    for i in range(1,size):
        inc[i]=inc[i-1]+1 if arr_elements[i]>=arr_elements[i-1] else 1
    
    #construct a decreasing sequence array
    for i in range(size-1,-1,-1):
        dec[i]=dec[i+1]+1 if arr_elements[i]>=arr_elements[i+1] else 1
    
    #find the length of max length bitonic sequence
    max = inc[0]+dec[0]-1
    for i in range(1,n):
        if (inc[i]+dec[i]-1>max):
             max=inc[i]+dec[i]-1
    return max


#input 2-d array in python
def inputArray(r):
    matrix=[]
    for _ in range(r):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix

def printMatrix2(matrix,r,c):
    for x in range(r):
        matrix[x].reverse()
    for x in range(r):
        for y in range(c):
            print(matrix[y][x],end=' ')
        print()


def printMatrix(matrix,r,c):
    for x in range(r):
        for y in range(c):
            print(matrix[y][x],end=' ')
        print()


def binary_search(la,k,l,search):
    while k<=l:
        m=(k+l)//2
        if la[m]==search:
            return 1
        elif la[m]>search:
            #l+=1
            l=m-1
        else:
            k=m+1
    return 0
        
    
def matrixSearch(arr,r,c,element_search):
    for i in range(r):
        if binary_search(arr[i],0,len(arr[i])-1,element_search):
            print("1")
            break
    else:
        print("0")

#how to swap elements of an array
#how to invert an image

def printMatrix3(matrix,r,c):
    matrix.reverse()
    for x in range(r-1):
        for y in range(c-1):
            #print(matrix[y][x],end=' ')
            matrix[y][x+1],matrix[x][y+1]=matrix[x+1][y],matrix[y][x+1]
        #print()
    print(matrix)

        '''
        for y in range(c):
            print(matrix[x][y],end=" ")
        '''
        #print()
    
    
#spiral array 
#inputting the array

#is it possible with the 2 pointers?
#we will have to work accordingly


def spiralPrint(r,c,a):
    k=0
    l=c-1
    m=r-1
    n=0
    while k<=m and n<=l :
        i=k
        j=n
        while i<=m:
            print(a[i][n],end=', ')
            i+=1
        j+=1
        while j<=l:
            print(a[m][j],end=', ')
            j+=1
        i=m-1
        while i>=k:
            print(a[i][l],end=', ')
            i-=1
        j=l-1
        #i+=1
        while j>n :
            print(a[k][j],end=', ')
            j-=1
        k+=1
        n+=1
        l-=1
        m-=1
    print("END")


def addDigits(num):
    co=0
    while num:
        rem = num%10
        num = num//10
        co+=rem
    return co
#find all the subset of a set, how is it possible?



if __name__=="__main__":
    
    t= int(input())
    while t!=0:
        n = int(input())
        #element_list=[int(input()) for _ in range(n)]
        element_list=list(map(int,input().split()))
        print(maxLengthBitonic(n,element_list))
        t-=1
        #res=formBiggestNumber(element_list)
    
    '''
    target = int(input())
    num_dict=targetSumPair(element_list,n,target)
    count=0
    for k,v in num_dict.items():
        if k in element_list and v in element_list and count < n//2:
            print(k,"and",v)
            count+=1
    '''
    
    'abba'
    



def spiralOrder(matrix,row,col):
    print(row,col)
    k = 0
    l = col-1
    m = row-1
    n = 0
    while k <= m and n <= l:
        #i=k+1
        j=n
        #printing first row
        while j <= l:
            print(matrix[k][j],end=',')
            j+=1
        #printing last column
        #i=i+1
        while i <=m:
            print(matrix[i][l],end=',')
            i+=1
        #printing last row
        #j-=2
        while j>=n:
            print(matrix[m][j],end=',')
            j-=1    
        #print first column
        i-=2
        while i>k:
            print(matrix[i][n],end=',')
            i-=1
        k+=1
        l-=1
        m-=1
        n+=1

def spiralOrderCorrect(matrix,row,col):
    print(row,col)
    k = 0
    l = col-1
    m = row-1
    n = 0
    while k <= m and n <= l:
        #i=k+1
        j=n
        #printing first row
        while j <= l:
            print(matrix[k][j],end=',')
            j+=1
        #printing last column
        #i=i+1
        k+=1
        i=k
        while i <=m:
            print(matrix[i][l],end=',')
            i+=1
        #printing last row
        l-=1
        j=l
        if m>=k:
            while j>=n:
                print(matrix[m][j],end=',')
                j-=1    
            m-=1
        #print first column
        if l>=n:
            i=m
            while i>=k:
                print(matrix[i][n],end=',')
                i-=1        
            n+=1
            


def chewbackNumber(num):
    st=[]
    while num:
        ans = num%10
        if 9-ans > ans:
            st.append(ans)
        else:
            st.append(9-ans)
        num=num//10
    while st:
        print(st.pop(0),end='')

a = int(input())
st=[]
while num:
    ans = num%10
    if 9-ans > ans:
        st.append(ans)
    else:
        st.append(9-ans)
    num=num//10
        