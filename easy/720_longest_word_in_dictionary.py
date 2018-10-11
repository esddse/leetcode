class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        prefixes = set(words)
        lgst_word = ""
        for word in prefixes:
            check = True
            for i in range(len(word), 0, -1):
                prefix = word[:i]
                if prefix not in prefixes:
                    check = False
                    break
            if check:
                if len(word) > len(lgst_word):
                    lgst_word = word
                elif len(word) == len(lgst_word) and word < lgst_word:
                    lgst_word = word
        return lgst_word