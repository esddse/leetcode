from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=cmp_to_key(lambda a, b: int(a+b) - int (b+a)), reverse=True)
        ans = "".join(nums).lstrip("0")
        return ans or "0" 