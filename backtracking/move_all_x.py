def move_all_x(s,b,e):
    
    if b>=e: return
    
    if s[b]=='x':
        n=b
        while n<e:
            s[n],s[n+1]=s[n+1],s[n]
            n+=1
        move_all_x(s,b,e-1)
    else:
        return move_all_x(s,b+1,e)

if __name__ == '__main__':
    n=input()
    n=list(n)
    move_all_x(n,0,len(n)-1)
    print(''.join(n))