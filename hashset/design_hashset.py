class Node:
    def __init__(self,key=None,next=None):
        self.key=key
        self.next=next
class MyHashSet:

    def __init__(self):
        self.bucket_size=997
        self.bucket = [Node() for _ in range(self.bucket_size)]
    
    def _hash(self,key):
        return key%self.bucket_size     

    def add(self, key: int) -> None:
        #calculate hash
        bucket_index = self._hash(key)
        node = self.bucket[bucket_index]
        # what if the element already exists
        if node.key is None:
            node.key=key
            return
        while node:
            if node.key==key:
                return
            if node.next is None:
                node.next=Node(key)
                return
            node = node.next
        
    def remove(self, key: int) -> None:

        bucket_index = self._hash(key)
        temp=self.bucket[bucket_index]
        prev=None
        if temp.key==key:
            if temp.next:
                # it is not the only element
                self.bucket[bucket_index]=temp.next
            else:
                # if it is the only element
                self.bucket[bucket_index] = Node()
            return

        while temp :
            if temp.key==key:
                prev.next=temp.next
                return
            prev=temp
            temp = temp.next
 
    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        node=self.bucket[bucket_index]
        while node:
            if node.key==key:
                return True
            node=node.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
res=obj.contains(2)
print(res)
#param_3 = obj.contains(key)
# obj.remove(1)
# print(obj.contains(1))