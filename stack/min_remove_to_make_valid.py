class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st1=[]
        st2=set()
        for i,char in enumerate(s):
            if char == ')':
                if st1 :
                    st1.pop()
                else:
                    st2.add(i)
            elif char=='(':
                st1.append(i)
        st2.update(st1)
        ans = [char for i,char in enumerate(s)  if i not in st2]
        return  "".join(ans)

        