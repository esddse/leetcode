from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0
        max_odd = 0
        for c, cnt in Counter(s).most_common():
            if cnt % 2 == 1:
                if cnt > max_odd:
                    max_odd = cnt
                else:
                    length += cnt - 1
            else:
                length += cnt
        return length + max_odd

        