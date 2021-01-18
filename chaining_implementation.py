'''
implement a chaining functionality in python 
1- It needs to do hashing in
2- search an element
3- insert an element
4- remove an element

find the challenge with the chaining?


'''


class Chaining:
    
    def __init__(self,bucket_size):
        self.size=bucket_size
        self.bucket =[[] for _ in range(bucket_size)]
    
    
    def insert(self,elem):
        hashNum = elem%self.size
        self.bucket[hashNum].append(elem)
        
    
    def remove(self,elem):
        hashNum=elem%self.size
        if self.search(elem):
            self.bucket[hashNum].remove(elem)
        else:
            return 'Element not present'
            
    
    def search(self,elem):
        #searching an element here
        hashNum = elem%self.size
        return elem in self.bucket[hashNum]
    
    
if __name__ == '__main__':
    
    ch =Chaining(7)
    ch.insert(4)
    ch.insert(7)
    ch.insert(49)
    ch.insert(56)
    ch.insert(1)
    ch.insert(2)
    ch.insert(3)
    ch.insert(4)
    ch.insert(5)
    ch.insert(6)
    print(ch.size)
    print(ch.bucket)
    print(ch.search(4),ch.search(76))
    ch.remove(49)
    print(ch.remove(100))
    print(ch.bucket)
    