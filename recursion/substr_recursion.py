def recursive_print(ip,op=''):
    if ip=='': 
        print(op)
        return 
    recursive_print(ip[1:],op)
    recursive_print(ip[1:],op+ip[0])
    
if __name__=='__main__':
    
    recursive_print('abc','')
    