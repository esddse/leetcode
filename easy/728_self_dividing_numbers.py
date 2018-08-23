class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        def check(num):
            raw = num
            while num >= 10:
                divisor = num % 10
                if divisor == 0 or raw % divisor != 0:
                    return False
                num //= 10
            return raw % num == 0

        selected = []
        for num in range(left, right+1):
            if check(num):
                selected.append(num)
        return selected
