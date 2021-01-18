
class Employee:
    
    notice='Sunday is a working day'
    
    def __init__(self,name,salary,email):
        self.name=name
        self.salary=salary
        self.email=email
        
    def showNotice(self):
        print(self.name,self.salary,self.email)
        
    def floatNotice(self):
        print(self.notice)
    
    @classmethod
    def updateNotice(cls,updatedNotice):
        cls.notice=updatedNotice
        
    @classmethod
    def showName(cls):
        return cls.name
    
    @classmethod
    def createInstance(cls,stringobject):
        name,salary,email = stringobject.split('-')
        return cls(name,salary,email)
    
    
    
    def __str__(self):
        return '{} is an instance of employee'.format(self.name)
    

if __name__=='__main__':
    """
    emp1 = Employee('Mridul',60000,'pantm@vmware.com')
    emp2= Employee('Srini',670000,'sreddygadam@vmware.com')
    
    emp1.showNotice()
    print(emp1,emp1.notice)
    emp2.showNotice()
    print(emp2,emp2.notice)
    emp1.notice='2 months notice period'#here we have tried to update the class variable using the instance variable then the class variable will not get updated as it needs 
    '''
    to be updated only by the className , in the above case again an object will get created as notice which is specific to the instance.
    
    
    '''
    print('after changing through the instance variable')
    emp1.floatNotice()
    emp2.floatNotice()
    #Employee.notice='2 months notice period which was initially as 3 months'
    Employee.updateNotice('2 months np left')
    print('after changing through the class variable')
    emp1.floatNotice()
    emp2.floatNotice()
    print('accessing through the instance variable')
    print(emp1.notice,emp2.notice)
    #how can we override this variable with the class variable
    
    print('to check the attributes created ')
    print(emp1.__dict__)
    print(emp2.__dict__)
    #there will be always a difference that will come up when we try to access the class variables
    #using the objects or the class name
  
    '''
    bigger understanding from this demo:
    never access the class variable using the instance 
    '''
    stringO= 'kavya-6000-kavya@gmail.com'
    emp3 = Employee.createInstance(stringO)
    print(emp3.showNotice())
    
    """
    
    emp1=Employee('Mridul',1000,'pantm@vmware.com')
    emp2=Employee('Kavya',20000,'kavya@gmail.com')
    try:
        print(emp1.showName())
        emp1.showNotice()
        print(emp2.showName())
        emp2.showNotice()
    except Exception as e:
        print(e)
    