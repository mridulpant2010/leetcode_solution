def stock_span(ar):
    st=[]
    new_ar=[]
    for i in range(len(ar)):
        if i==0:
            new_ar.append(-1)
        elif len(st)>0 and st[-1]>ar[i]:
            ind=ar.index(st[-1])
            new_ar.append(ind)
        elif len(st)>0 and st[-1]<=ar[i]:
            while len(st)>0 and st[-1]<=ar[i]:
                st.pop()
            new_ar.append(-1) if len(st)==0 else new_ar.append(ar.index(st[-1]))
        st.append(ar[i])
    for i in range(len(ar)):
        new_ar[i]= i-new_ar[i]
        #yield new_ar[i]
    #print(*new_ar)
    
def stock_span_leetcode(ar,st,new_ar,i):
    if len(st)==0:
        new_ar.append(-1)
    elif len(st)>0 and st[-1]>ar:
        ind=ar.index(st[-1])
        new_ar.append(ind)
    elif len(st)>0 and st[-1]<=ar:
        while len(st)>0 and st[-1]<=ar:
            st.pop()
        new_ar.append(-1) if len(st)==0 else new_ar.append(ar.index(st[-1]))
    st.append(ar)
    new_ar[i]= i-new_ar[i]
    i+=1
    yield new_ar[i]


if __name__=='__main__':
    #n=int(input())
    ar=[100 ,80, 60, 70, 60, 75, 85]
    stock_span(ar)
    #list= 