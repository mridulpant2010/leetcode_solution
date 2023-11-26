from machinecoding.service.serviceImpl.cache import CacheBuilding
import sys


if __name__ == '__main__':
    c =  CacheBuilding()
    c.put('1','first')
    c.put('2','second')
    c.put('3','third')
    c.put('4','fourth')
    print(c)
    print(c.get('2'))
    print(c.get('3'))
    print(c.delete('4'))
    print(c)