
def toString(l):
    return ''.join(l)
def permute(st,l,r):
    if l==r:
        print(st)
    else:
        for i in range(l,r+1):
                st[l],st[i]=st[i],st[l]
                permute(st,l+1,r)
                st[l],st[i]=st[i],st[l]
                

if __name__=='__main__':
    permute([1,2,3],0,2)
                