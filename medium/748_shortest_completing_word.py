class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        license_clean = [c.lower() for c in licensePlate if c.lower() in alphabet]

        def check(license, word):
            word_lower = word.lower()
            checked = [False] * len(word) 
            for c in license:
                found = False
                for i, word_c in enumerate(word):
                    if checked[i]:
                        continue
                    if c == word_c:
                        found = True
                        checked[i] = True
                        break
                if not found:
                    return False
            return True

        min_len  = float('inf')
        min_word = None
        for word in words:
            if check(license_clean, word):
                if len(word) < min_len:
                    min_len = len(word)
                    min_word = word 
        return min_word