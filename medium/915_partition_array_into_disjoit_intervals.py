class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        size = len(A)

        min_right = [float("inf")] * size
        min_num = float("inf")
        for i in range(size-1, -1, -1):
            min_right[i] = min(min_num, A[i])
            min_num = min_right[i]

        max_left = [0] * size
        max_num = 0
        for i in range(size):
            max_left[i] = max(max_num, A[i])
            max_num = max_left[i]
            if max_left[i] <= min_right[i+1]:
                return i+1