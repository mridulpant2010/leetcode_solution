

class Person:
    
    def __init__(self,name):
        self.name=name
        print('person class constructor')
        
    def __str__(self):
        return 'class: Person'
    
    
class Student(Person):
    
    #since student class is using the attributes and the method from the base class, we cannot repeat the methods and the attribute.
    #let's try to use the inheritance     
    def __init__(self,name,age):
        super().__init__(name)
        #whenever you do the inheritance the base class constructor is called,first the base class is called then the child class is called.

        self.age=age
        print('Student class constructor')
    
    def __str__(self):
        return 'class: Student'    

#how to create  the abstract classes in python?


if __name__=='__main__':
    
    p=Person('Mridul')
    s=Student('Mridul',23)
    print(s.name,s)
    print(p.name,p)
    


