class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        p, q, spq, min_len = 0, 0, 0, float("inf")
        while q < size:
            while q < size and spq < s:
                spq += nums[q]
                q += 1
            if q == size and spq < s:
                break
            while spq - nums[p] >= s:
                spq -= nums[p]
                p += 1
            min_len = min(min_len, q-p)
            spq -= nums[p]
            p += 1
        return min_len if min_len != float("inf") else 0
            