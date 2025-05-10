class Node:
    def __init__(self,key=None,value=None,next=None):
        self.key=key
        self.value=value
        self.next=next

class HashMap:
    def __init__(self):
        self.size=997
        self.hash_table = [Node() for _ in range(self.size)]
        
    
    def _hash(self,key):
        # it calculates the index of the given key.
        return hash(key)%self.size
        
    
    def put(self, key, value):
        index = self._hash(key)
        node =  self.hash_table[index]
        # check if the key already exists in the linkedlist.         
        if node.key is None:
            node.key = key
            node.value = value

        while node:
            # if the key of  element already exists, update the values
            if node.key==key:
                node.value = value
                return
            else:
                node.next= Node(key,value)
            node = node.next
        return
               
    
    def get(self,key):
        index = self._hash(key)
        node = self.hash_table[index]
        while node:
            if node.key==key:
                return node.value
            node=node.next
        return -1

    
    def remove(self,key):
        index = self._hash(key)
        node = self.hash_table[index]
        # removing the element from the beginning
        if node.key==key:
            if node.next:
                self.hash_table[index]=node.next # if it isn't the only element
            else:
                # if it is the only element
                self.hash_table[index]=Node()
            return
        
        prev=None
        while node:
            if node.key==key:
                prev.next=node.next
                return
            prev=node
            node=node.next
        
# the edge cases when the code doesn't exists.
if __name__ == "__main__":
    hashmap = HashMap()
    hashmap.put("apple", 1)
    hashmap.put("banana", 2)
    hashmap.put("grape", 3)
    
    
    #print("HashMap:", hashmap)
    print("Get 'apple':", hashmap.get("apple"))
    print("Get 'banana':", hashmap.get("banana"))
    print("Get 'grape':", hashmap.get("grape"))
    print("Get 'orange':", hashmap.get("orange"))

    hashmap.remove("banana")
    print("Get 'banana':", hashmap.get("banana"))
    #print("HashMap after removing 'banana':", hashmap)