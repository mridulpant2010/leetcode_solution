def string_permutation(inp,i,j,n):
    
    if i==n:
        #print()
        a_set.add(''.join(inp))
        return 
        
    for j in range(i,n):
        inp[i],inp[j]=inp[j],inp[i]
        string_permutation(inp,i+1,j,n)
        inp[i],inp[j]=inp[j],inp[i]
    
    
    #handling the special case of getting the duplicates
    

if __name__ == '__main__':
    a_set=set()
    inp=input()
    string_permutation(list(inp),0,0,len(inp))
    for el in sorted(a_set):
        print(el)