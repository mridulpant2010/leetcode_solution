from flask import Flask
from machinecoding.service.serviceImpl import CacheBuilding


#learn basics of flask to tackle these kind of theings.


'''
following questions are inside my mind that how will you
    - cache size overflow 
    - how to implement the cache eviction, that is the main thing over here.
'''
'''
things to keep in mind while designing for a new service
- specific status code
- exception handling strategy
- handling concurrency?
- multi threaded application

'''
'''
- python best practices
- restful best practices


'''

@Get("cache/v1/get/{}") 
statuscode = 200 if exists
statuscode = 404 not found

@Put("cache/v1/add/", requestbody=True) 
statuscode = 201 if exists
statuscode = 404 not found

@delete("cache/v1/delete")
statuscode = 200 if exists
statuscode = 404 not found