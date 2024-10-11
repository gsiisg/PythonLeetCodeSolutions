class TrieNode():
    def __init__(self):
        self.child = {} # alternative ways to implement PrefixTrie: https://www.geeksforgeeks.org/trie-insert-and-search/
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.child:
                node.child[letter] = TrieNode()
            node = node.child[letter]
        node.end = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter in node.child:
                node = node.child[letter]
            else:
                return False
        if node.end:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter in node.child:
                node = node.child[letter]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)