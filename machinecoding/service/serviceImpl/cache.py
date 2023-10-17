from requests import delete
from machinecoding.exceptions.notfound import NotFoundException
from machinecoding.service.cache_service import CacheService
# class CacheBuilding:
# 	def __init__(self):
# 		self.obj = {}

# 	def get(self,k):
#      if k not in self.obj.keys():
#          throw NotFoundException("Key doesn't exists")
#      return self.obj[k]
		
# 	def put(self,k,value):
# 		self.obj[k] = value
	    
# 	def delete(self,k):
# 		self.obj.pop(k)
	
# 	def __str__(self):
# 		return self.obj



# if __name__ == "__main__":	
#     CacheBuilding cache = new CacheBuilding()
# 	cache.put(1,'first')
# 	cache.put(2,'second')
# 	print(cache)

class CacheBuilding(CacheService):
    def __init__(self,capacity):
        self.obj = dict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.obj.keys(): 
            raise NotFoundException("cache not found")
        return self.obj[key]
    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            self.evict(key)
        self.obj[key] = value
    def delete(self, key):
        if key not in self.obj.keys(): 
            raise NotFoundException("cache not found")
        return self.obj.pop(key)
    def __str__(self):
        return self.obj.__str__()
    def clear(self):
        self.obj = {}
    
    def evict(self, key):
        #evict only when the capacity is crossed.
        # FIFO based cache eviction
        if key not in self.obj.keys(): 
            raise NotFoundException("cache not found")
        remove_key = next(iter(self.obj))
        return delete(key)
    
            
    
# learning how to write a SOLID design pattern for the same.