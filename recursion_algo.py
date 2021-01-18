#writing about the merge-process from the merge-sort


def merge(a,l,m,r):
    left= a[l:m+1]
    right=a[m+1:r+1]
    i=0
    j=0
    k=l #why is k value as l
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            a[k]=left[i]
            i+=1
        else:
            a[k]=right[j]
            j+=1
        k+=1
    
    while i < len(left):
        a[k]=left[i]
        k+=1
        i+=1
        
    while j<len(right):
        a[k]=right[j]
        k+=1
        j+=1
    return a

def merge_sort(a,l,r):
    if l<r:
        m=(l+r)//2
        merge_sort(a,l,m)
        merge_sort(a,m+1,r)
        merge(a,l,m,r)