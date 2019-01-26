class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {")": "(", "]": "[", "}": "{"}

        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in pair and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return not stack