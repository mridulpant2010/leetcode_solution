class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_set_pat = set()
        hash_set_s = set()
        hash_map = dict()
        li_s=s.split(" ")
        for char in pattern:
            if char not in hash_set_pat:
                hash_set_pat.add(char)
        for word in li_s:
            if word not in hash_set_s:
                hash_set_s.add(word)
        
        hash_map=dict(zip(list(hash_set_pat),list(hash_set_s)))
        print(hash_map)
        try:
            for i in range(len(pattern)):
                mapped_word = hash_map.get(pattern[i])
                if mapped_word != li_s[i]:
                    return False 
        except IndexError:
            return False
        #return True
        return len(hash_set_pat)==len(hash_set_s) and len(pattern)==len(li_s)
        

if __name__=='__main__':
    solution = Solution()
    print(solution.wordPattern("jquery","jquery")) # True