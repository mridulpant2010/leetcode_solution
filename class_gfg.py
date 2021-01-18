class Dog:
    #class-variable
    animal='Dog'
    
    def __init__(self,breed,color):
        #instance-variable
        self.__breed=breed
        self.__color=color
        #how can we do data-hiding in python
        #we can use thedouble_score (__) before the attributes name and those attributs will not directly visible outside.
        #how to make methods private in python?
    def __repr__(self):
        pass
    
    def __str__(self):
        pass
    
    


if __name__ == '__main__':
    Rodger= Dog('Pug','brown')
    Buzo = Dog('Bulldog','black')
    print(Rodger.__breed,Rodger.__color)
    print(Dog.animal)
        