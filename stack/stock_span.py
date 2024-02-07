#https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

class Solution:
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        st=[(a[0],0)]
        res=[1]
        #code here
        for i in range(1,len(a)):
            if a[i]<st[-1][0]:
                res.append(i-st[-1][1])
            elif a[i]>=st[-1][0]:
                while len(st)>0 and a[i]>=st[-1][0]:
                    st.pop()
                if len(st)==0:
                    res.append(i+1)
                else:
                    res.append(i-st[-1][1])
            
            
            st.append((a[i],i))
        return res