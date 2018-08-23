class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter

        A = A.split(" ")
        B = B.split(" ")
        words = A + B

        counter = Counter(words)
        uncommon = []
        for word, cnt in counter.items():
            if cnt == 1:
                uncommon.append(word)
        return uncommon
