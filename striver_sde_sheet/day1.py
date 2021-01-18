
#seggregate zeros and one in python using the below code
def seggregate_zero_one(arr):
 start=0
 end=len(arr)-1
 while start<=end:
  if arr[start]==1 and arr[end]==0:
   arr[start],arr[end]=arr[end],arr[start]
  elif arr[start]==0:
   start+=1
  elif arr[end]==1:
   end-=1
 print(arr,start,end)
 
 
#dutch 

#merge 2 sorted list in python

a = [[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]

def merge_intervals(arr):
    #sort the array 
    arr.sort(key=lambda x:x[0])
    max_element=arr[0]
    new_list=[]
    for elem in range(1,len(arr)):
        if max_element[0]==arr[elem][0] and max_element[-1]>arr[elem][-1]:
            elem+=1
        elif max_element[-1]<=arr[elem][-1] and max_element[0]<arr[elem][0] and max_element[-1]>=arr[elem][0]:
            new_list.append((max_element[0],arr[elem][-1]))
            max_element=new_list[-1]
        elif max_element[0]<arr[elem][0] and max_element[1] < arr[elem][1]: 
            new_list.append(tuple(arr[elem]))
            max_element=new_list[-1]
    list2=(list(set(new_list)))
    return [list(eachl) for eachl in list2]


#this question is similar to dutch flag problem
def sort_colors(arr):
    mid=0
    start=0
    end=len(arr)-1
    while mid <=end:
        if arr[mid]==0:
            arr[start],arr[mid]=arr[mid],arr[start]
            start+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[end],arr[mid]=arr[mid],arr[end]
            end-=1
    return arr
        

            