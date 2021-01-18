#give an example of the cyclic-reference in python
    #these are dangerous and might cause your program to crash

class firstClass:
    def __init__(self,name):
        self.name=name
    
class secondClass:
    
    def __init__(self):
        
        """
        Initializes the constructor for the second class
        """
        self.c = firstClass(self)
    
    #string overloading in python
    def __str__(self):
        """[summary]

        Returns:
            string: classname
        """
        print('str of second class is called')
        return 'second class name'
    
    def __del__(self):
        print('delete the constructor')
    

class Person:
    
    #creating slots in the class to avoid the use of the runtime instances in python
    #while creating objects in python there is a lot of memory that is created and that is saved 
    #If we uses the slots there are following benefits:
    '''
    1- it doesn't creates dictionary  the runtime, thus saves a lot of RAM.
    2- it doesn't allow attributes to be crated at the run time.
    '''
    __slots__ = ['name','__age','gender']
    
    def __init__(self,name,age,gender):
        """
        Initializes a constructor for the user
        """
        self.name = name
        self.__age=age  #is it a private or protected variable?
        self.gender=gender
        
        
    def __str__(self):
        """
        string formatting for the class
        """
        return 'class Name: Person'
    
    def getAge(self):
        return self.__age
    
    #so when you create a slot in python 
    #i guess it automatically removes the dict from the runtime.
    def showDict(self):
        return self.__dict__

# __ then you cannot access the variable outside the class


class Car:
    '''
    example to illustrate the functioning of 
    '''    
    def __init__(self,diesel_engine,company,price,owner):
        self.diesel_engine=diesel_engine
        self.company = company
        self._price=price
        self.__owner=owner
        
        
class Hyundai(Car):
    def __init__(self,engine,company,price,owner):
        super().__init__(engine,company,price,owner)
    def getCar(self):
        print('diesel_engine',self.diesel_engine)
        print('company name is',self.company)
        print('price is',self._price)




h = Hyundai('true','hyundai',100000,'mridul')
h.getCar()
print(h._price)
print(h.__owner)


#what is the use of metaprogramming?

'''
metaprogramming is the code which manipulates code.

class method vs static method in python?

what is the difference in both and when to use one?
properties of the class:
1-state 
2-attributes

'''

from datetime import date

class Person:
    
    def __init__(self,age,name):
        self.age=age
        self.name=name
        
        #if self is a python defined keyword ?
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

        #if cls is a python defined keywornd
    @staticmethod
    def isAdult(age):
        return age>18
    
    
if __name__=='__main__':
    
    p =Person(23,'Mridul')
    print(p.age,p.name)
    
    
    

