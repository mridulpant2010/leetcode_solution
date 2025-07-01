def permutation(st,start,v):
    if start == len(st)-1:
        v.append(''.join(st))
        return
    mp =set()
    for i in range(start,len(st)):
        if st[i] not in mp:
            mp.add(st[i])
            st[start], st[i] = st[i], st[start]
            permutation(st,start+1,v)
            st[start], st[i] = st[i], st[start]
    return v
        
            

if __name__ == "__main__":
    #mp = set()
    ans = permutation(["a","b","c"],0,[])
    print(ans)