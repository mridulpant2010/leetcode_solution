# Code a data structure which allows us to store and retrieve items by key up to a fixed capacity. When we add items over capacity we free up space by removing an item first: 
# 1) remove any expired item first 
# 2) If there are no expired items, find the items with the lowest priority number, and remove the one which has been used least recently of them Optimise for time.
from collections import defaultdict
class Node:
    def __init__(self,key,value,next=None,prev=None):
        self.key=key
        self.value = value
        self.next=next
        self.prev=prev
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count=0
    def addToEnd(self,key,value):
        newNode = Node(key,value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail = self.tail.next
        self.count+=1
        
    def delete(self,node):
        if self.tail is None:
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.count-=1
        #edge condition when 
    def moveToEnd(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.tail.next=node
        node.prev= self.tail
        self.tail=self.tail.next
        #edge condition when head is null or when tail is null.

class ElementNotFoundException(Exception):
    pass

class LRUCache(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = defaultdict(DoublyLinkedList)
        self.storage = DoublyLinkedList()
        self.count=0
    def add(self,key,value):
        if self.count>=self.capacity:
            element = self.storage.pop(0)
            del self.cache[element]
        self.cache[key]=value
        self.storage.append(key)
        self.count+=1
    def remove(self,key):
        #if the cache is empty, remove
        ans = self.search(key)
        del self.cache[key]
        self.storage.remove(key)
        self.count-=1
    def get(self,key):
        try:
            if key in self.cache:
                self.storage.remove(key)
                self.storage.append(key)
        except KeyError:
            raise ElementNotFoundException
    def display(self):
        for k,v in self.cache.items():
            print(k,v)
        print(self.storage)
#find the shortcomings and bugs in this code 

if __name__ == '__main__':
    cache = LRUCache(5)
    cache.add(1,"mridul")
    cache.add(2,"shubham")
    cache.add(3,"kavya")
    cache.add(4,"lata")
    cache.add(5,"navin")
    cache.get(1)
    cache.display()
    cache.add(6,"rishabh")
    cache.display()