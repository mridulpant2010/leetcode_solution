class Node:
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev = prev
        self.next = next


class ArrayBoundException(Exception):
    pass

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addAtBeginning(self,value):
        # least recently used node is always at the end and the most recent one is at the front.
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        #self.length+=1
        return node
        
    def remove(self,node):
        # remove node from the beginning
        prev_node = node.prev
        if prev_node:
            prev_node.next = node.next
        else:
            # if node.next:
            #     node.next.prev = prev_node
            self.head = node.next
            
        next_node = node.next
        if next_node:
            next_node.prev = prev_node
        else:
            # if node.prev:
            #     node.prev.next = next_node
            self.tail = prev_node
        node.prev = node.next = None
        # condition when self.tail is None
class LRU:
    def __init__(self,capacity):
        self.size = capacity
        self.hash_map = {}
        self.doubly_ll = DoublyLinkedList()

    
    def put(self,key,value):
        if len(self.hash_map) <= self.size:
            if key in self.hash_map:
                node = self.hash_map[key]
                node.val = value
                self.doubly_ll.remove(node)
                new_node = self.doubly_ll.addAtBeginning(node.val)
                del self.hash_map[key]

            else:
                # node doesn't exist
                new_node = self.doubly_ll.addAtBeginning(value)
            self.hash_map[key] = new_node
        else:
            raise ArrayBoundException
    
    def get(self,key):
        if key in self.hash_map:
            node=self.hash_map[key]
            self.doubly_ll.remove(node)
            new_node = self.doubly_ll.addAtBeginning(node.val)
            del self.hash_map[key]
            self.hash_map[key] = new_node
            return node.val
        else:
            return -1
    
if __name__=="__main__":
    lru_cache = LRU(10)
    lru_cache.put(1,2)
    lru_cache.put(2,3)
    lru_cache.put(3,4)
    lru_cache.get(2)
    lru_cache.get()
    
