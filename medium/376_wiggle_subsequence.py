class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        pos, neg = [1] * size, [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] - nums[j] > 0:
                    pos[i] = max(pos[i], neg[j]+1)
                elif nums[i] - nums[j] < 0:
                    neg[i] = max(neg[i], pos[j]+1)
        return max(pos+neg)