class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        digits = "0123456789"
        if str[0] in digits:
            sign = 1
        elif str[0] == "+":
            sign = 1
            str = str[1:]
        elif str[0] == "-":
            sign = -1 
            str = str[1:]
        else:
            return 0

        num = ""
        for c in str:
            if c in digits:
                num += c
            else:
                break
        if not num:
            return 0
        num = sign * int(num)

        num = -(1<<31) if num < -(1<<31) else num
        num = (1<<31)-1 if num > (1<<31)-1 else num
        return num 

