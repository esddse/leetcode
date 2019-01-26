class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        c2w, w2c = {}, {}
        for i in range(len(pattern)):
            c, w = pattern[i], words[i]
            if c not in c2w and w not in w2c:
                c2w[c] = w 
                w2c[w] = c 
            elif c in c2w and w in w2c and c2w[c] == w and w2c[w] == c:
                continue
            else:
                return False 
        return True
            
