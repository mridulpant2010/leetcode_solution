def THO(n, source, dest, aux):
    if n == 1:
        print("Moving ring 1 from", source, "to", dest)
        return  
    else:
        THO(n - 1, source, aux, dest)
        print("Moving ring", n, "from", source, "to", dest)
        THO(n - 1, aux,dest, source)

n= int(input())
THO(n, 'A', 'B','C' )