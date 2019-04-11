class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [c.lower() for c in s if (c.lower() >= 'a' and c.lower() <= 'z') or (c >= '0' and c <= '9')]
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True