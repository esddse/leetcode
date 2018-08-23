class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"

        rows = [row1, row2, row3]
        def check(word, rows):
            for row in rows:
                if all([c in row for c in word]):
                    return True
            return False

        return [word for word in words if check(word, rows)]