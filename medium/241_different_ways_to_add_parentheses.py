
from itertools import product
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        def compute(input):
            if "+" not in input and not "-" in input and not "*" in input:
                return [int(input)]
            res = []
            for i in range(len(input)):
                if input[i] == "+":
                    for a, b in product(compute(input[:i]), compute(input[i+1:])):
                        res.append(a + b)
                elif input[i] == "-":
                    for a, b in product(compute(input[:i]), compute(input[i+1:])):
                        res.append(a - b)
                elif input[i] == "*":
                    for a, b in product(compute(input[:i]), compute(input[i+1:])):
                        res.append(a * b)
            return res

        return compute(input)