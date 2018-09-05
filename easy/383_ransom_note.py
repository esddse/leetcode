
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransom_counter  = Counter(ransomNote)
        magzine_counter = Counter(magazine)

        for key, cnt in ransom_counter.items():
            if cnt > magzine_counter[key]:
                return False
        return True
        