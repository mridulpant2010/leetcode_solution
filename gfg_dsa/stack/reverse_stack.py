def reverse_stack(st):
 i=0
 new_st=[]
 while i < len(st):
  top_e = st.pop()
  j = len(st)-1
  while j>=i:
   new_st.append(st.pop())
   j-=1
  st.append(top_e)
  #print(st,new_st)
  while len(new_st)>0:
   st.append(new_st.pop())
  i+=1
 return st

if __name__ == '__main__' :
	n = int(input())
	st =[]
	for _ in range(n):
		st.append(int(input()))
	output=reverse_stack(st)
	while len(output)>0:
		print(output.pop())