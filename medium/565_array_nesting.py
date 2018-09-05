class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mark = {}
        for num in nums:
            mark[num] = 0

        for num in nums:
            if not mark[num]:
                i = 1
                k = num
                while not mark[k]:
                    mark[k] = i
                    k = nums[k]
                    i += 1

        return max([cnt for num, cnt in mark.items()])

