class Person:
    
    def __init__(self):
        self.name=name
        self.age=age
        
    def m1(self):
        print('m1 from parent')
        
class Teacher(Person):
    
    def __init__(self,name,age,specialization):
        super().__init__(name,age)
        self.specialization=specialization
    
    def display(self):
        print(self.name,self.age,self.specialization)
        
        
------------------------
def subArraySum(arr,n,given_sum):
    start=0
    end=0
    sum_till_now=0
    while end<n:
        if sum_till_now<given_sum:
            sum_till_now+=arr[end]
            end+=1
        elif sum_till_now==given_sum:
            return (start+1,end)
        else:
            sum_till_now-=arr[start]
            start+=1
    return False