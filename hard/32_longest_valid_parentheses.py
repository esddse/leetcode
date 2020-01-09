
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        sum2idx = {}
        accu_sum, max_len, thr = 0, 0, -1
        for i, c in enumerate(s):
            if c == "(":
                accu_sum += 1
                if accu_sum-1 not in sum2idx:
                    sum2idx[accu_sum-1] = i-1
                    thr = min
            else:
                accu_sum -= 1
                if accu_sum in sum2idx:
                    max_len = max(max_len, i-sum2idx[accu_sum])
                for s in [s for s in sum2idx if s > accu_sum]:
                    del sum2idx[s]
        return max_len 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        max_len = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                l = 0
                while stack and type(stack[-1]) == int:
                    l += stack.pop()
                if stack and stack[-1] == "(":
                    l += 2
                    stack.pop()
                    while stack and type(stack[-1]) == int:
                        l += stack.pop()
                    max_len = max(max_len, l)
                    stack.append(l)
        return max_len
                