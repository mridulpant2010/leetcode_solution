from collections import defaultdict
def checkInclusion(s1,s2):
    j=0
    d=defaultdict(int)
    for el in s1:
        d[el]+=1
    count=len(s1)
    k=len(s1)
    i=0
    ans=0
    while j<len(s2):
        if s2[j] in d.keys():
            d[s2[j]]-=1
            if d[s2[j]]==0:
                count-=1

        elif j-i+1<k:
            j+=1
        elif j-i+1==k:
            if count==0:
                print(s2[i],s2[j])
                ans+=1
            if s2[i] in d.keys():
                d[s2[i]]-=1
                if d[s2[i]]!=0:
                    count+=1
            j+=1
            i+=1
    return ans


def checkInclusions(s1,s2):
    d=defaultdict(int)
    e=defaultdict(int)
    for el in s1:
        d[el]+=1
    for el in s2:
        e[el]+=1
    print(e)
    for i in range(len(s2)):
        c=s2[i]
        if c in d.keys() and d[c]!=e[c]:
            print(d[c],e[c],c)
            return False
    return True
s1='ab'
s2='eidbaooo'
print(checkInclusion(s1,s2))