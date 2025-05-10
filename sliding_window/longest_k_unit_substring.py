#https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

from collections import defaultdict
    
# def longestKSubstr(s, k):
#     # code here
#     max_len=-1
#     map = defaultdict(int)
#     end=0
#     start=0
#     while end < len(s):
#         map[s[end]]+=1
#         if len(map)<k:
#             end+=1
#         elif len(map)==k:
#             max_len = max(max_len,end-start+1)
#             end+=1
#         else:
#             while len(map)>k:
#                 print(map)
#                 print(start,end)
#                 map[s[start]]-=1
#                 if map[s[start]]==0:
#                     del map[s[start]]
#                 start+=1
#     return max_len

def longestKSubstr( s, k):
    # code here
    start=0
    end=0
    max_len=-1
    hash_map=defaultdict(int)
    while end<len(s):
        hash_map[s[end]]+=1
        if len(hash_map)<k:
            end+=1
        elif len(hash_map) == k:
            max_len = max(max_len,end-start+1)
            end+=1
        else:
            while len(hash_map)>k :
                hash_map[start]-=1
                if hash_map[s[start]]==0:
                    del hash_map[s[start]]
                start+=1   
            end+=1
    return max_len


if __name__ == "__main__":
    s="aabacbebebe"; K = 3
    #K=2
    ans = longestKSubstr(s,K)
    print(ans)
    



        
