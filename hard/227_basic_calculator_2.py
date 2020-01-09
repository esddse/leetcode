class Solution:
    def calculate(self, s: str) -> int:

        def get_num(s, i):
            digits = "1234567890"
            num = ""
            while i < len(s) and s[i] in digits:
                num += s[i]
                i += 1
            return int(num) if num else None, i
        s = s.replace(" ", "")
        size = len(s)
        stack = []
        num, i = get_num(s, 0)
        stack.append(num)
        while i < size:
            if s[i] == "*":
                num1 = stack.pop()
                num2, i = get_num(s, i+1)
                stack.append(num1 * num2)
            elif s[i] == "/":
                num1 = stack.pop()
                num2, i = get_num(s, i+1)
                stack.append(int(num1/num2))
            elif s[i] == "+":
                 stack.append("+")
                 num, i = get_num(s, i+1)
                 stack.append(num)
            elif s[i] == "-":
                 stack.append("-")
                 num, i = get_num(s, i+1)
                 stack.append(num)
        num = stack[0]
        size, i = len(stack), 1
        while i < size:
            if stack[i] == "+":
                num += stack[i+1]
            else:
                num -= stack[i+1]
            i += 2
        return num