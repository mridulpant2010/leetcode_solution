def InfixtoPostfix(exp):
    st=[]
    d={
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3,
        '(':0
    }
    operator_list=d.keys()
    for each_el in exp:
        if each_el not in operator_list and each_el not in ['(',')']:
            print(each_el,sep='',end='')
        elif each_el in operator_list or each_el =='(':
            if len(st)==0 or  each_el =='(' :
                st.append(each_el) 
            elif   d[each_el]>d[st[-1]]:
                st.append(each_el)
            elif d[each_el]<=d[st[-1]]:
                while len(st)>0 and d[each_el]<=d[st[-1]]:
                    print(st[-1],sep='',end='')
                    st.pop()
                st.append(each_el)
        else:
            if each_el==')':
                while len(st)>0 and st[-1]!='(':
                    print(st[-1],sep='',end='')
                    st.pop()
                st.pop()
            
            #print(st,each_el)
    while len(st)>0:
        print(st[-1],sep='',end='')
        st.pop()
        
        


InfixtoPostfix('A*(B+C)/D')