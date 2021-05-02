import json
d= {
	"username": "Martin",
	"favoriteNumber":1337,
	"interests":["daydreaming","hacking"]
}

d_json=json.dumps(d)


#write msgpack file
import msgpack

with open("sample.msgpack","wb") as outfile:
 packed= msgpack.packb(d)
 outfile.write(packed)
 
 
#read from the msgpack 

f=open("sample.msgpack","rb").read()

#if encoding is really important ,then why?
'''
1- encoding is compression.
2- encoding is cross-language or cross-platform.

'''

#pickle vs msgpack 
'''
pickle-- numerical data or anything uses buffer protocol, can do the classes and functions
msgpack-- cross language interoperation , faster for text data and python objects better than pickle
'''

import pickle

with open('sample_pickle.pickle','wb') as outfile:
 #outfile.write(pickle.dumps(d))
 pickle.dump(d,outfile)
 
d_pickle=open('sample_pickle.pickle').read()


import hashlib

def encrypt_string(hash_string):
    sha_signature=hashlib.sha256(hash_string.encode()).hexdigest()
    print(sha_signature)
    with open('password.txt','wb') as outfile:
        outfile.write(sha_signature.encode())
    return sha_signature

sha_signature=encrypt_string('nikita')
print(sha_signature)

with urllib.request.urlopen('http://tinyurl.com/api-create.php?') as response:
    html = response.read().decode('utf-8')
    print(html)

def improved_encrypt_string():
    user
    password='nikita'
    salt=os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,10000)
    #store them as 
    storage=salt+key
    print("salt",storage[32:])
    print("key",storage[:32])