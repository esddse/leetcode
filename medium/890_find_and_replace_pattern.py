class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        outputs = []
        for word in words:
            if len(word) != len(pattern):
                continue
            pattern2word = {}
            word2pattern = {}
            valid = True
            for i in range(len(pattern)):
                if pattern[i] not in pattern2word:
                    if word[i] not in word2pattern:
                        pattern2word[pattern[i]] = word[i]
                        word2pattern[word[i]] = pattern[i]
                    else:
                        valid = False
                        break
                else:
                    if word[i] != pattern2word[pattern[i]]:
                        valid = False
                        break
            if valid:
                outputs.append(word)
        return outputs