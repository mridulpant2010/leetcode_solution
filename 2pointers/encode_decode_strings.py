class Solution:

    def encode(self, strs):
        if len(strs)==0: return []
        s=""
        for el in strs:
            s =s + str(len(el))+"#"+el
        return s

    def decode(self, s: str):
        if s=="":
            return []
        res=[]
        i=0#int(s[0])
        while i<len(s) :
            j = i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            start=j+1
            end = start+length
            res.append(s[start:end])
            print(num,s[start:end],i)
            i=end
            print(i)
        return res


s = Solution()
#strs=["neet","code","love","you"]
strs = ["we","say",":","yes","!@#$%^&*()"]
encode_string=s.encode(strs)
# for i,str in enumerate(encode_string):
#     print(i,str)
print(encode_string)
decoded_string = s.decode(encode_string)
print(decoded_string)
