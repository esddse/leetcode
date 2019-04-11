class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return -1
        if len(A) != len(B):
            return -1
        size = len(A)
        s = set([A[0], B[0]])
        cnt = {A[0]:{"A":0, "B":0}, B[0]:{"A":0,"B":0}}
        for i in range(size):
            s &= set([A[i], B[i]]) 
            if A[i] in s:
                cnt[A[i]]["A"] += 1
            if B[i] in s:
                cnt[B[i]]["B"] += 1

        min_ret = float("inf")
        for k, v in cnt.items():
            a, b = v["A"], v["B"]
            diff = a + b - size 
            if diff >= 0:
                ret = min(a, b) - diff
                min_ret = min(min_ret, ret)
        if min_ret == float("inf"):
            return -1
        return min_ret