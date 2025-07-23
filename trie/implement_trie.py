# https://leetcode.com/problems/implement-trie-prefix-tree/
class TreeNode:
    def __init__(self):
        self.eow=False
        self.child={}

class Trie:
    def __init__(self):
        self.root=TreeNode()
        
    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.child:
                temp.child[char]=TreeNode()
            temp = temp.child[char]
        temp.eow=True
        
    def search(self, word: str) -> bool:
        temp = self.root
        for char in word:
            if char not in temp.child:
                return False
            temp = temp.child[char]
        return temp.eow

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for char in prefix:
            if char not in temp.child:
                return False
            temp = temp.child[char]
        return True   


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)