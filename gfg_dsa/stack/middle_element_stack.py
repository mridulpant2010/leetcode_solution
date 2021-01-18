from collections import deque

def solve(st,k):
    if k==1:
        st.pop()
        return st
    temp=st[-1]
    st.pop()
    k-=1
    solve(st,k)
    st.append(temp)
    return st

if __name__=='__main__':
    st=[1,2,3,4,5]
    k=len(st)//2+1
    a=solve(st,k)
    print(a)