class Node:
    def __init__(self):
        self.char_to_node = {}
        self.end_flag = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        def add_to_trie(word, node):
            if word == "":
                node.end_flag = True
                return 
            if word[0] not in node.char_to_node:
                node.char_to_node[word[0]] = Node()
            add_to_trie(word[1:], node.char_to_node[word[0]])
        add_to_trie(word, self.trie)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_in_trie(word, node):
            if word == "":
                if node.end_flag:
                    return True
                else:
                    return False
            if word[0] == ".":
                for c, nxt in node.char_to_node.items():
                    if search_in_trie(word[1:], nxt):
                        return True
                return False
            else:
                if word[0] not in node.char_to_node:
                    return False
                return search_in_trie(word[1:], node.char_to_node[word[0]])
        return search_in_trie(word, self.trie)
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)