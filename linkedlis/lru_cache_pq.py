import heapq
import time


class Node:
    def __init__(self,key,value,prev=None,next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def moveToEnd(self,node):
        if self.tail == node or node.next is None:
            return 
        
        if node.prev is None:
            self.head = self.head.next
        else:
            node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.next=node
        node.prev = self.tail
        self.tail=self.tail.next
    
    def addToLast(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev = self.tail
            self.tail= self.tail.next
    
    def remove(self,node):
        if node.prev is None:
            self.head=self.head.next
        if node.next is None:
            self.tail=self.tail.prev
        
        if node.prev:
            node.prev.next=  node.next
        if node.next:
            node.next.prev = node.prev
        

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.storage=DoubleLinkedList()
        self.priority_queue = []
        
    def get(self,key):
        if key in self.cache:
            expiration_time = self.cache[key]["expiration_time"]
            node = self.cache[key]["data"]
            if expiration_time < time.time():
                #evict the node
                self.storage.remove(node)
                del self.cache[key]
                print("node evicted")
                return None
            else:
                #move the node to end of the DLL
                self.storage.moveToEnd(node)
                return node.value
        else:
            return -1
        
    def put(self,key,value,expiration_time):
        if key in self.cache:
            #update the element in the cache 
            node = self.cache[key]["data"]
            node.value = value
            heapq.heappush(self.priority_queue,(expiration_time,key))
            self.cache[key] = {"data":node,"expiration_time":expiration_time}
            self.storage.remove(node)
            self.storage.addToLast(node)
            
        else:
            if len(self.cache)>=self.capacity:
                #evict the node based on the expiration time and LRU
                expired_time,key=heapq.heappop(self.priority_queue)
                print(expired_time,key)
                if expired_time < time.time():
                    node = self.cache[key]["data"]
                    del self.cache[key]
                    self.storage.remove(node)
                    print("expiration_time")
                else:
                    #removing the first node.
                    node = self.storage.head
                    self.storage.remove(node)
                    del self.cache[key]
                    print("priority")
            
            node = Node(key,value)
            self.cache[key] = {"data":node,"expiration_time":expiration_time}
            self.storage.addToLast(node)
            heapq.heappush(self.priority_queue,(expiration_time,key))
            
            # add new element to the cache.
        

if __name__ == "__main__":
    cache = LRUCache(2)
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