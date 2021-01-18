'''
method 1: to create the hashmap injection

'''


'''
example of a decorator in python
1- we have func f
2- we have to enhance the f functionality but by adding some more pattern to it

'''
import sys

def check_func(inp_func):
    #import pdb;pdb.set_trace()
    def inside(a,b):
        if b==0:
            print('cannot use the function more')
        else:
            return inp_func(a,b)
    return inside        

def func(a,b):
    return a/b

b=check_func(func)
print(b(5,3))

@check_func
def add(a,b):
    return a/b

print(add(3,2))

#when we want to add an extra functionality to our python code, we can use this 




'''
hash map 
'''

class Setting:
    
    def __init__(self,url=None,api_key=None):
        self.url=url
        self.api_key=api_key

class Sensor:
    
    def __init__(self):
        pass
    
    def __str__(self):
        return "Sensor object"


#define objects(instances) of your classes inside the hash-map


class Controller:
    
    def __init__(self,hashmap):
        self.hashmap=hashmap
    
    def __str__(self):
        return 'Controller class'

    
if __name__ == '__main__':
    
    
    d={
    'sensor' : Sensor(),
    'settings' :Setting(url='google.com',api_key='12313')
    
    }

    c= Controller(d)
    print(c.hashmap.get('sensor'))




#defining the static function in python 
'''

'''