def balanced_paranthesis(ar):
    d = {')':'(',']':'[','}':'{'}
    st=[]
    for each_element in ar:
        if each_element in ['(','{','[']:
            st.append(each_element)
        else: 
            if len(st)>0 and d[each_element]==st[-1] :
                st.pop()
            else:
                st.append(each_element)
    return len(st)==0
    