class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k <= 1:
            return 0

        length = len(nums)
        cnt = 0
        ll, lr = -1, -1
        l, r, product = 0, 0, 1
        while l < length:
            # find maximal
            if l < r:
                product /= nums[l]
                l += 1
            while r < length and product < k:
                product *= nums[r] 
                r += 1
            if product >= k:
                r -= 1 
                product /= nums[r]
            interval_sum = lambda x, y: (y-x+1) * (y-x) // 2
            cnt += interval_sum(l, r)
            if lr > l:
                cnt -= interval_sum(l, lr)
            ll, lr = l, r
            if r < length:
                product *= nums[r]
                r += 1
        return cnt