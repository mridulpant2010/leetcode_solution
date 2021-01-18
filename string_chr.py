def lowerUpper(single_chr):
    if ord(single_chr) in range(65,91):
        print(chr(ord(single_chr)+32))
    elif ord(single_chr) in range(97,123):
        print(chr(ord(single_chr)-32))
    elif ord(single_chr) in range(48,58):
        print(chr(single_chr))
    else:
        print("Invalid")


def characterType(single_chr):
    if ord(single_chr) in range(65,91):
        print("U")
    elif ord(single_chr) in range(97,123):
        print("L")
    else:
        print("I")



def stringDifferenceAscii(s):
    li=[]
    i=0
    j=i+1
    while j<len(s):
        li.append(s[i])
        d=ord(s[j])-ord(s[i])
        #print(s[i],d)
        li.append(str(d))
        i+=1
        j=i+1
    li.append(s[j-1])
    ans=''.join(li)
    print(ans)
    
def sanketString(k,strn):
    d=dict()
    for i in strn:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    res= sorted(d.items(),key=lambda x:x[1])
    #print(res)
    dif=res[0][1]-k
    if dif==0:
        dif=res[0][1]
    #print(dif,res[0][1],res[1][1])
    max_perfectness=res[1][1]+dif
    print(max_perfectness)


def stringCompression(strn):
    list_elements=[]
    d=dict()
    for i in strn:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    for k,v in d.items():
        list_elements.append(k)
        list_elements.append(str(v))
    st=''.join(list_elements)
    print(st)
    
'''
character arrays 

palindromic ,check whehter a string is palindrome or not
--we can also solve this question using 2-pointer technique
'''

def isPalindrome(strn):
    if len(strn)==0 or len(strn)==1:
        return True
    i=0
    j=len(strn)-1
    while i<j:
        if strn[i]==strn[j]:
            i+=1
            j-=1
        else:
            return False
    return True


def isPalindromerecursive(strn,i,j):
    
    #base-case
    if strn[i]
    #recursive calls
    if strn[i]==strn[j]:
        return isPalindromerecursive(strn,i+1,j-1)
    else:
        return False
    #self-work
    

def canyouReadThis(strn):
 ran=[]
 for x in range(0,len(strn)):
  if strn[x].isupper():
   ran.append(x)
 i=0
 j=1
 print(strn[:ran[i]])
 while j<len(ran):
  print(strn[ran[i]:ran[j]])
  i=j
  j+=1
 print(strn[ran[i]:])
  
  
 
 return ran




def stringRemoveDuplicate(strn):
    str_l=list(strn)
    i=0
    j=1
    if str_l ==0 or str_l ==1:
        return str_l
    while j<len(str_l)-1:
        if str_l[j]!=str_l[i]:
            i+=1
            str_l[i]=str_l[j]
        j+=1
    str_l[i+1]=str_l[j]
    print(str_l[:i+2],i,j)
    #str_l[i+1]=str_l[j]
    #st=''.join(str_l[:i+2])
    #return st
    
#converting the existing code 


def findLargestString(k):
    
    max_largest=0
    largest_str=None
    for _ in range(k):
        a=input()
        if len(a)>max_largest:
            largest_str=a
            max_largest=len(a)
    print(largest_str)
            

def stringCompression(strn):
    strn+='0'
    i=0
    j=1
    count=1
    while j <len(strn):
        if strn[i]==strn[j]:
            j+=1
            count+=1
        else:
            print(strn[i],count)
            i=j
            count=0
        
    

        

if __name__=='__main__':
    #k = int(input())
    num_chr=int(input())
    str_list=[input() for _ in range(num_chr)]
    single_chr= ''.join(str_list)
    #sanketString(k,single_chr)
    #stringCompression(single_chr)
    print(isPalindrome(single_chr))