def insertAtBottom(st,top):
    if len(st)==0: 
        st.append(top)
        return
    d=st.pop()
    insertAtBottom(st,top)
    st.append(d)

def reverse_stack(st):
    if len(st)==0: return
    
    top=st.pop()
    reverse_stack(st)
    #st.append(top)
    insertAtBottom(st,top)

if __name__ == '__main__':
    #st=[3,2,1]
    n= int(input())
    st=[]
    for _ in range(n):
        st.append(int(input()))
    reverse_stack(st)
    #print(st)
    while len(st)>0:
        print(st.pop())