
import copy
import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        new = copy.deepcopy(self.origin)
        random.shuffle(new)
        return new


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()