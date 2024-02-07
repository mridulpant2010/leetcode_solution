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
        if node.prev is None:
            self.head=self.head.next
        if node.next is None:
            self.tail=self.tail.prev
        
        if node.prev:
            node.prev.next=  node.next
        if node.next:
            node.next.prev = node.prev
        self.count-=1
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.key," -> ",temp.value,sep="\t")
            temp = temp.next
            
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.storage= DoubleLinkedList()
        
    def get(self, key: int) -> int:
        if key in self.cache:
            get_node  = self.cache[key]
            self.storage.remove(get_node)
            self.storage.addToLast(get_node)
            return get_node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value=value
            self.storage.remove(node)
        else:
            if len(self.cache)>=self.capacity :
                #self.storage.display()
                node = self.storage.head
                self.storage.remove(node)
                self.storage.display()
                print(" eviction completed ")
                if node.key in self.cache:
                    print("key ->",self.cache.pop(node.key).key)
            node = Node(key,value)
            self.cache[key]=node
        self.storage.addToLast(node)
        
if __name__ == "__main__":
    ip=["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    param=[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    
    cache = LRUCache(10)
    for k,v in zip(ip,param):
        if k=="put":
            cache.put(v[0],v[1])
        elif k=="get":
            print(v[0],cache.get(v[0]))