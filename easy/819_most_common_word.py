
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = paragraph.lower()
        punctuations = "!?',;."
        for p in punctuations:
            paragraph = paragraph.replace(p, "")
        counter = Counter(paragraph.split(" "))
        for word, cnt in counter.most_common():
            if word not in banned:
                return word
        