import abc

class CacheService(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get(self, key):
        pass
    
    @abc.abstractmethod
    def delete(self, key):
        pass
    
    @abc.abstractmethod
    def put(self, key,value):
        pass