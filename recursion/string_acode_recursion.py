def generate_string(ip,op):
    
    if ip=='':
        print((op.upper()))
        return 
    op1=op
    op2=op
    ip1=ip
    ip2=ip
    digit=int(ip[0])
    digit2=int(ip[0:2])
    #print(digit,digit2)
    ch=hash_table[digit]
    #print(ip,ch,digit2,digit)
    ip1=ip1[1:]
    generate_string(ip1,op1+ch)
    if digit2 <=26 and len(ip2)>1:
        ch2=hash_table[digit2]
        #print('op2',op2,ch2)
        ip2=ip2[2:]
        generate_string(ip2,op2+ch2)
    return

if __name__ == "__main__":
    hash_table={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    av=input()
    generate_string(av,'')