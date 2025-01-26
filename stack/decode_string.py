# i think i will have to write a more recursive code. Let us do it on our own, challenge my limits and get things done.
class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        curr=0
        concat_st=''
        while curr < len(s):
            #print(s[curr],st)
            if s[curr]=='[':
                curr+=1
                while s[curr]!=']':
                    concat_st = concat_st+s[curr]
                    print(concat_st)
                    curr+=1
            elif s[curr] == ']':
                top = st.pop()
                #print(top,concat_st)
                concat_st = concat_st * int(top)
                #print(concat_st)
                st.append(concat_st)
                curr+=1
                concat_st=''
            else:
                st.append(s[curr])
                curr+=1
        new_chr=''
        while len(st)>0:
            top = st.pop()
            new_chr = top + new_chr
        return new_chr
    
    
class Solution:
    
    def decodeString(self,s):
        self.decode(s,0,[],'')
    
    
    def decode(self,s,curr,st,concat_str):
        if s[curr]=='[':
            curr+=1
            concat_str = concat_str + s[curr]
        elif s[curr] == ']':
            top = st.pop()
            concat_str = concat_str * int(top)
            st.append(concat_str)
            curr+=1
            concat_str=''
        else:
            st.append(s[curr])
            curr+=1
        self.decode(s,curr,st,concat_str)
            
            
        