from collections import defaultdict
def find_anagrams(a, b):
  hash_b = defaultdict(int)
  new=[]
  for k in b:
    hash_b[k]+=1
  b_len=len(hash_b)
  #print(hash_b)
  for i in range(len(a)-b_len+1):
    hash_a = defaultdict(int)
    for j in range(i,i+b_len):
      hash_a[a[j]]+=1
      #print(i,j,a[j],hash_a)
      if hash_a==hash_b:
        new.append(i)
    
  # Replace this placeholder return statement with your code
  return new

def find_anagram(a,b):
    out=[]
    if len(a)<len(b):
        return out
    hash_a= defaultdict(int)
    hash_b= defaultdict(int)
    start=0
    end=0
    for i in range(len(b)):
        hash_b[b[i]]+=1
    while end<len(a):
        hash_a[a[end]]+=1
        end+=1
        print(hash_a)
        if (end-start)==len(hash_b):
            if hash_a==hash_b:
                out.append(start)
            hash_a[a[start]]-=1
            if hash_a[a[start]]==0:
                del hash_a[a[start]]
            start+=1
    return out
        

if __name__=="__main__":
    a = "acttacttca"
    b = "cat"
    new = find_anagram(a,b)
    print(new)