class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        stack = []

        for s in S:
            if s == "(":
                stack.append(s)
            else:
                num = 0
                while stack[-1] != "(":
                    num += stack.pop()
                num *= 2
                stack.pop()
                if num == 0:
                    num = 1
                stack.append(num)
            # print(stack)

        return sum(stack)
