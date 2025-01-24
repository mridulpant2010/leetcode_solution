class HashMap:
    ''' A hash table implementation
    '''
    
    def __init__(self,size=10):
        self.hash_table = [[] for _ in range(size)]
        self.size=size
    
    def _hash(self,key):
        # it calculates the index of the given key.
        return hash(key)%self.size
        
    
    def put(self, key, value):
        ''' how the index is calculated , how the hash of the key is calculated to return the index.
            what is the collision resolution strategy.
            
        '''
        index = self._hash(key)
        bucket =  self.hash_table[index]
        
        #what if the code already exists in the hash table.
        # how this address pass by reference is working.
        for i,(k,v) in enumerate(bucket):
            if k==key:
                self.hash_table[index][i] = (key,value)
                return 

        self.hash_table[index].append((key,value))
        # what will be the difference between the self.hash_table.append() and the bucket.append() function
        # what collision resolution strategy is used here.
        
    
    def get(self,key):
        index = self._hash(key)
        bucket = self.hash_table[index]
        for k,v in bucket:
            if k==key:
                return v
        return -1
    
    def remove(self,key):
        index = self._hash(key)
        bucket = self.hash_table[index]
        for i,(k,v) in enumerate(bucket):
            if k==key:
                del bucket[i]
                return
        
        
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