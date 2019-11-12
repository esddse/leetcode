class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for c in preorder.split(","):
            stack.append(c)
            # check 
            while len(stack) >= 3 and stack[-1]=="#" and stack[-2]=="#":
                if stack[-3] == "#":
                    return False
                else:
                    stack.pop()
                    stack.pop()
                    stack[-1] = "#"
        if len(stack) == 1 and stack[0] == "#":
            return True 
        return False

