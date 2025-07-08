class Solution:
    def ngl(self,heights):
        st = [(heights[0],0)]
        ngl_ar=[-1]
        for i in range(1,len(heights)):
            if heights[i]<st[-1][0]:
                ngl_ar.append(st[-1][1])
            elif heights[i]>=st[-1][0]:
                while len(st)>0 and heights[i]>=st[-1][0]:
                    st.pop()
                st.append((heights[i],i))
                if len(st)>0:
                    ngl_ar.append(st[-1][1])
                else:
                    ngl_ar.append(-1)
        return ngl_ar

    
if __name__=="__main__":
    s = Solution()
    height=[1,7,2,5,4,7,3,6]
    ans = s.ngl(height)
    print(ans)