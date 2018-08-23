class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        output = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            if stack:
                day_top, temp_top = stack[-1]
                while temp_top < temp:
                    output[day_top] = day - day_top
                    stack.pop()
                    if not stack:
                        break
                    day_top, temp_top = stack[-1]
            stack.append((day, temp))
        return output

                    