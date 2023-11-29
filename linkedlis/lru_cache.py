class Node:
    def __init__(self,key,value,next=None,prev=None):
        self.key=key
        self.value=value
        self.next=next
        self.prev=prev

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def addToLast(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev = self.tail
            self.tail=self.tail.next
        self.count+=1
        
    def remove(self,node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head=node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail=node.prev
        self.count-=1
        return node

    def moveToEnd(self,node):
        if self.tail == node or node.next is None:
            return
        if node.prev is None:
            self.head = node.next
        else:
            prev = node.prev
            prev.next = node.next
            # if node.next:
            #     node.next.prev = prev
        node.next.prev = node.prev
        self.tail.next=node
        node.prev = self.tail
        self.tail = self.tail.next
    def display(self):
        temp = self.head
        while temp:
            print(temp.key," -> ",temp.value)
            temp=temp.next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.storage= DoubleLinkedList()
        
    def get(self, key: int) -> int:
        if key in self.cache:
            get_node  = self.cache[key]
            self.storage.moveToEnd(get_node)
            self.storage.display()
            return get_node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value=value
            node=self.storage.remove(node)
            print(" updated node")
        else:
            if len(self.cache)>=self.capacity :
                #eviction of the nodes
                #node = self.cache[key]
                node=self.storage.remove(self.storage.head)
                print(" eviction ")
                print(node.key,node.value)
                del self.cache[node.key]

            node = Node(key,value)
            self.cache[key]=node
        self.storage.addToLast(node)


if __name__=='__main__':
    obj = LRUCache(2)
    
    # print(obj.get(2))
    # obj.put(2,6)
    # print(obj.get(1))
    # obj.put(1,5)
    # obj.put(1,2)
    # print(obj.get(1))
    # print(obj.get(2))
    # print(obj.cache)
    
    #[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    obj.put(2,1)
    obj.put(2,2)
    print(obj.get(2))
    obj.put(1,1)
    obj.put(4,1)
    print(obj.get(2))
    # print(obj.cache)