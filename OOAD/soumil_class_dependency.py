

#class injection model
#what is the benefit and advantage of using it?
#when can we use it and when should we not use it?

class Setting():
    
    def __init__(self,url=None,api_key=None):
        self.url=url
        self.api_key=api_key
    

class Sensor():
    
    def __init__(self,instance):
        
        self.instance = instance
        self.myurl=self.instance.url
        print("accessing the url from the ",self.myurl)
        

class Sensor2:
    
    def __init__(self):
        self.instance= Setting('abc.com','12345321')

    def __str__(self):
        return 'Sensor2 object'
    

'''
method 1: we created the object and injected into the second class instance -- injecting the classes

method2 : we have called the first class object in the second class
'''
s2= Sensor2()
print(s2)