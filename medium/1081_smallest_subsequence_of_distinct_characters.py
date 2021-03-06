class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last_idx = {c:i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and stack[-1] > c and last_idx[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        return "".join(stack)



