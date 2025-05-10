def first_unique_char(s):

    # Replace this placeholder return statement with your code
    hash_map = {}
    hash_set= set()
    #pos=-1
    for i in range(len(s)):
        if s[i] in hash_set:
            try:
                del hash_map[s[i]]
            except KeyError:
                continue
        else:
            hash_map[s[i]]=1
            hash_set.add(s[i])
    print(hash_map)
    for pos,i in enumerate(s):
        if i in hash_map.keys():
            return pos
    return -1

if __name__=="__main__":
    s="goodmorning"
    res= first_unique_char(s)
    print("index is ",res)