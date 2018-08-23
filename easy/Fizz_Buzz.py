class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(n):
            num = i+1
            if num % 15 == 0:
                lst.append("FizzBuzz")
                continue
            elif num % 3 == 0:
                lst.append("Fizz")
                continue
            elif num % 5 == 0:
                lst.append("Buzz")
                continue
            else:
                lst.append(str(num))
                
        return lst
            