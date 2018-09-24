
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
                
        product  = 0
        char_set = {}
        for i in range(len(words)):
            if words[i] not in char_set:
                char_set[words[i]] = set(words[i])
            for j in range(i+1, len(words)):
                if words[j] not in char_set:
                    char_set[words[j]] = set(words[j])
                if not char_set[words[i]] & char_set[words[j]]:
                    product = max(product, len(words[i]) * len(words[j]))
        return product