

'''
1- creating function
2- understanding static function

more on static-method:
1- static-method are more bound towards a class rather than its object.
2- they can access the properties of a class
3- it is a utility function that doesn't need access any properties of a class but makes sense that it belong to a class,we use static functions.


'''

class Person:
    
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return 'Person Object {}'.format(self.name)
    
    @staticmethod
    def stat_method():
        a=10
        print('bro, I am a static method and please don"t try to access me from an instance ')
        print(a)

if __name__=='__main__':
    
    p =Person('mridul')
    print(p)
    
    p.stat_method()
    Person.stat_method()