class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res, cur = float("-inf"), float("-inf")
        for i, v in enumerate(A):
            res = max(res, cur + v)
            cur = max(cur, v) - 1
        return res
            