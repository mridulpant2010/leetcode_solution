from collections import defaultdict

def return_max_element(ar):
	d=defaultdict(int)
	for el in ar:
		d[el]+=1
	max_e=-10000
	for k,v in d.items():
		max_e= max(v,max_e)
	for k,v in d.items():
		if v==max_e:
			return k


if __name__=='__main__':
	d=int(input())
	b=list(map(int,input().split()))
	print(return_max_element(b))
