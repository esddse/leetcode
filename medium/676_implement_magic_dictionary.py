
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.words = set([])
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for word in dict:
            for i in range(len(word)):
                for c in alphabet:
                    if word[i] != c:
                        new_word = word[:i] + c + word[i+1:]
                        self.words.add(new_word)

        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """

        if word in self.words:
            return True
        else:
            return False


        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)