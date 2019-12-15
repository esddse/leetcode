class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, float("inf")]
        ret = ""
        k -= 1
        for i in range(n):
            c, k = divmod(k, factorial[n-i-1])
            ret += str(nums[c])
            nums.pop(c)
        return ret

