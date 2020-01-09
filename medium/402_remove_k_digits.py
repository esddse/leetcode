class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        if k >= size:
            return "0"
        new_num = ""
        stack = []
        for c in num:
            if not stack or k == 0 or c >= stack[-1]:
                stack.append(c)
            else:
                while stack and k > 0 and c < stack[-1]:
                    stack.pop()
                    k -= 1
                stack.append(c)
        return  "".join(stack[:len(stack)-k]).lstrip("0") or "0"