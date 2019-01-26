import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        
        s = 1
        for i in range(2, math.ceil(num ** 0.5)):
            if num % i == 0:
                if i == math.ceil(num ** 0.5):
                    s += i 
                else:
                    s += i + num / i 

        if s == num:
            return True 
        else:
            return False