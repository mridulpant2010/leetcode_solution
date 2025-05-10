from collections import defaultdict
def is_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    hash_map = defaultdict(int)
    for each_char in str1:
        hash_map[each_char]+=1
    
    for each_char in str2:
        hash_map[each_char]-=1
    print(hash_map)
    count_val= sum([1 if value!=0 else 0 for value in hash_map.values()])
    return count_val==0

    
    
print(is_anagram("super","upper"))