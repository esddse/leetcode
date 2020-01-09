import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or len(nums) == 1 or k == 0:
            return False
        size = len(nums)
        k = min(k, size-1)
        window = sorted(nums[:k+1])
        for i in range(k):
            if window[i+1] - window[i] <= t:
                return True
        i, j = 0, k+1
        while j < size:
            # pop
            idxi = bisect.bisect_left(window, nums[i])
            window.pop(idxi)
            # insert
            num = nums[j]
            idxj = bisect.bisect_left(window, num)
            if idxj > 0 and num - window[idxj-1] <= t:
                return True
            if idxj < k and window[idxj] - num <= t:
                return True
            window.insert(idxj, num)
            i += 1
            j += 1
        return False