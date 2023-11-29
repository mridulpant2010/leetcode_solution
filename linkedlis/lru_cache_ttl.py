
import time
class Node:
    def __init__(self,key,value,next=None,prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def remove(self,node):
        #case1: extreme element
        if node.prev is None:
            #we are removing the starting element
            self.head = self.head.next
        if node.next is None:
            # we are removing the last element
            self.tail=self.tail.prev
        #case2: middle element
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
    def addAtLast(self,node):
        #adding the node at the end of the list
        #case1: if the head is empty , first element is added
        if self.head is None:
            self.head = node
            self.tail = node 
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
    
    def moveToEnd(self,node):
        #case1: if the element is already the last node
        #case2: if the element is middle 
        #case3: if the element is at the beginning
        if self.tail ==node or node.next is None:
            return 

        if node.prev is None:
            self.head = self.head.next
        else:
            node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.next=node
        node.prev = self.tail
        self.tail = self.tail.next
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.key,temp.value)
            temp=temp.next

class LRUCacheTTL:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.storage= DoublyLinkedList()
    def get(self,key):
        if key in self.cache:
            node  = self.cache[key]["data"]
            expiration_time = self.cache[key]["expiration_time"]
            if expiration_time < time.time():
                #eviction based on the expired item from the DLL. 
                self.storage.remove(node)
                del self.cache[node.key]
                print("node evicted")
                return None
            else:
                #evict node based on the priority
                self.storage.moveToEnd(node)
                return node.value
        else:
            return -1

    def put(self,key,value,expiration_time):
        if key in self.cache:
            #case for the updation
            node = self.cache[key]["data"]
            node.value = value
            self.storage.remove(node)
            self.cache[key]={"data":node,"expiration_time":expiration_time}
            #update the expiration time 
        else:
            if len(self.cache)>=self.capacity:
                # eviction based on the earliest expiration time
                oldest_key = min(self.cache, key=lambda x:self.cache[x]["expiration_time"])
                expiration = self.cache[oldest_key]["expiration_time"]
                if expiration < time.time() :
                    node = self.cache[oldest_key]["data"]
                    self.storage.remove(node)
                    del self.cache[node.key]
                else:
                    #eviction based on the priority
                    node = self.storage.head
                    self.storage.remove(node)
                    del self.cache[node.key]
            node = Node(key,value)
            self.cache[key]={"data":node,"expiration_time":expiration_time}
        self.storage.addAtLast(node)


if __name__ == "__main__":
    cache = LRUCacheTTL(2)
    # print(cache.get(2))
    # #cases that can be formed
    # cache.put(1,2,time.time()+5)
    # cache.put(3,4,time.time()+10)
    # print(cache.get(1))
    # time.sleep(6)
    # cache.put(2,3,time.time()+8)
    # print(cache.get(1)) 
    # print(cache.get(3))
    # print(cache.get(2))
    
    # # Wait for some time to let items expire
    # time.sleep(10)

    # # Try to retrieve an expired item
    # print(cache.get(3))
    # print(cache.get(2))
    
    #case 2 for eviction 
    print(cache.get(2))
    #cases that can be formed
    cache.put(1,2,time.time()+25)
    cache.put(3,4,time.time()+30)
    print(cache.get(1))
    time.sleep(6)

    print(cache.get(1)) 
    cache.put(2,3,time.time()+8)
    print(cache.get(3))
    print(cache.get(2))
    print(cache.get(1)) 