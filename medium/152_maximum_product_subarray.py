class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        size = len(nums)
        dp_max = [num for num in nums]
        dp_min = [num for num in nums]
        for i in range(1, size):
            dp_max[i] = max([nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i]])
            dp_min[i] = min([nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i]])
        return max(dp_max)