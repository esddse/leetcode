class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        def find(l, r):
            while 0<=l and r<size and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        size = len(s)
        max_len, max_str = 0, ""
        for i in range(size):
            odd_str = find(i, i)
            even_str = find(i, i+1)
            curr_str = odd_str if len(odd_str) > len(even_str) else even_str
            if len(curr_str) > max_len:
                max_len = len(curr_str)
                max_str = curr_str 
        return max_str

        