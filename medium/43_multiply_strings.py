class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        size1, size2 = len(num1), len(num2)
        num1 = list(map(int, num1))
        num2 = list(map(int, num2))
        num1.reverse()
        num2.reverse()

        def add(lst1, lst2):
            if len(lst1) < len(lst2):
                lst1, lst2 = lst2, lst1
            ret = []
            carry = 0
            for i in range(len(lst2)):
                num = lst1[i] + lst2[i] + carry
                ret.append(num % 10)
                carry = num // 10
            for i in range(len(lst2), len(lst1)):
                num = lst1[i] + carry
                ret.append(num % 10)
                carry = num // 10
            if carry:
                ret.append(carry)
            return ret

        def mult(lst, c):
            ret = []
            carry = 0
            for i in range(len(lst)):
                num = lst[i] * c + carry
                ret.append(num % 10)
                carry = num // 10 
            if carry:
                ret.append(carry)
            return ret

        ret = []
        for i, c2 in enumerate(num2):
            c2 = int(c2)
            d = [0] * i + mult(num1, c2)
            ret = add(ret, d)
        while len(ret) > 1 and ret[-1] == 0:
            ret.pop()
        return "".join(map(str, reversed(ret)))

