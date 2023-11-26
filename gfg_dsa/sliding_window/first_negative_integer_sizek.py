#https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1


def printFirstNegativeInteger( A, N, K):
    # code here
    start=0
    end=0
    while end <N:
        while end-start+1<=K and end>=K-1:
            if A[start]<0:
                print(A[start])
                break
            elif start==end:
                print(0)
                break
            else:
                start+=1
        if (end-start+1) > K:
            start+=1
        else:
            end+=1
            
if __name__ == '__main__':
    N = 8
    A=[12, -1, -7, 8, -15, 30, 16, 28]
    K = 3
    printFirstNegativeInteger( A, N, K)
    
    N = 5
    A=[-8, 2, 3, -6, 10]
    K = 2
    printFirstNegativeInteger( A, N, K)