from abc import ABC,abstractmethod

class User(ABC):
    
    '''
    is the user-class really an abstract one?
    which all the methods will be considered for the abstraction? 
    '''
    
    def __init__(self,userId,name,password):
        self.__userId=userId
        self.__name=name
        #need to take care for the password activities
        self.__password=password
    
    def __str__(self):
        return 'User class is called'
    
    @abstractmethod
    def getUserId(self):
        return self.__userId
    
    @abstractmethod
    def getName(self):
        return self.__name
    