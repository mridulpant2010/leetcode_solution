def sort(arr,i,n):
	if i>=n:
		return arr
	sort_recursive(arr,i,i+1,n)
	sort(arr,i+1,n)
def sort_recursive(arr,i,j,n):
	if j>=n:
		return arr
	if arr[i]>arr[j]:
		arr[i],arr[j]=arr[j],arr[i]
	print(arr,i,j)
	sort_recursive(arr,i,j+1,n)