class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        if l1 > l2:
            num1 = "0" + num1
            num2 = "0" * (l1 - l2 + 1) + num2
        else:
            num1 = "0" * (l2 - l1 + 1) + num1
            num2 = "0" + num2

        carry = 0
        num = []
        for i, j in zip(num1[::-1], num2[::-1]):
            n = int(i) + int(j) + carry
            num.append(str(n%10))
            carry = n // 10
        num = "".join(reversed(num))

        if num == "0":
            return num
        if num[0] == "0":
            return num[1:]
        return num