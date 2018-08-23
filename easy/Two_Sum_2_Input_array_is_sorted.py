class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        h = len(numbers)-1
        while numbers[l] + numbers[h] != target:
            if numbers[l] + numbers[h] < target:
                l += 1
            else:
                h -= 1
        return [l+1, h+1]