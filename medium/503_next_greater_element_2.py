class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []

        greaters = [-1] * len(nums)
        stack = []
        i = 0
        while True:
            num = nums[i]
            if not stack:
                stack.append((num, i))
            else:
                while stack and num > stack[-1][0]:
                    num_top, pos = stack.pop()
                    greaters[pos] = num
                if (num, i) in stack:
                    break
                stack.append((num, i))

            i = (i+1) % len(nums)
        return greaters
