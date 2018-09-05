
from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter1 = Counter(s)
        counter2 = Counter(t)

        if counter1 == counter2:
            return True
        else:
            return False