class StockSpanner:
    
    def __init__(self):
        self.st=[]
        self.new_ar=[]
        self.i=0
        
    def next(self, ar: int) -> int:
        if len(self.st)==0:
            self.new_ar.append(-1)
        elif len(self.st)>0 and self.st[-1]>ar:
            ind=ar.index(self.st[-1])

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
    
