

from collections import defaultdict
def k_distinct_char(s,k):
    start=0
    end=0
    max_l=0
    dict = defaultdict(int)
    while end<len(s):
        dict[s[end]]+=1
        while len(dict.keys())>k:
            dict[s[start]]-=1
            if dict[s[start]]==0:
                del dict[s[start]]
            start+=1
        max_l = max(max_l,end-start+1)
        end+=1
    return max_l

if __name__ == "__main__":
    s = "aa"
    k=1
    res= k_distinct_char(s,k)
    print(res)