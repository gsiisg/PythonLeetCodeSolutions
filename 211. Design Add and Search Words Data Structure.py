class TrieNode():
    def __init__(self):
        self.child = {} # alternative ways to implement PrefixTrie: https://www.geeksforgeeks.org/trie-insert-and-search/
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.child:
                node.child[letter] = TrieNode()
            node = node.child[letter]
        node.end = True

    

    def search(self, word: str) -> bool:

        def recurse(word, node, index):

            if index == len(word):
                return node.end

            letter = word[index]

            # this will try dfs style all possible letters and if any one is True then return True, else try next letter
            if letter == '.':
                for child_node in node.child.values(): # important to have .values() here
                    if recurse(word, child_node,index+1):
                        return True
            
            elif letter in node.child.keys(): # important to have .keys() here
                return recurse(word, node.child[letter], index+1)

            return False

        return recurse(word, self.root, 0)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)