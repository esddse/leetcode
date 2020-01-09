class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        max_len = 0
        while counter:
            num = list(counter.keys())[0]
            del counter[num]
            l = num-1
            while l in counter:
                del counter[l]
                l -= 1
            r = num+1
            while r in counter:
                del counter[r]
                r += 1
            max_len = max(max_len, r-l-1)
        return max_len