import bisect
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        
        arr = [(a, i) for i, a in enumerate(A)]
        arr.sort()

        res = 0
        mini = arr[0][1]
        for a, i in arr[1:]:
            res = max(res, i-mini)
            mini = min(i, mini)

        return res