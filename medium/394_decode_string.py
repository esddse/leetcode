class Solution:
    def decodeString(self, s: str) -> str:

        size = len(s)
        p = 0
        stack = []
        while p < size:
            if s[p] == "]":
                string = ""
                while type(stack[-1]) == str:
                    string = stack.pop() + string
                number = stack.pop()
                stack.append(string*number)
                p += 1
            else:
                if s[p] == "[":
                    p += 1
                elif s[p].isdigit():
                    number = ""
                    while s[p].isdigit():
                        number += s[p]
                        p += 1
                    stack.append(int(number))
                else:
                    string = ""
                    while p < size and not s[p].isdigit() and s[p] not in "[]":
                        string += s[p]
                        p += 1
                    stack.append(string)

        return "".join(stack)