class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            num = digits[i] + carry
            carry = num // 10
            digits[i] = num % 10
        if carry == 1:
            digits = [1] + digits
        return digits