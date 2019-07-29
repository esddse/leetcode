class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        size = len(A)
        max_valid_lengths = []
        contiguous_min_lengths = []
        cnt_max, cnt_min = 0, 0
        for num in A:
            # 根据大于R的数分隔串
            if num > R:
                if cnt_max:
                    max_valid_lengths.append(cnt_max)
                    cnt_max = 0
            else:
                cnt_max += 1

            # 连续的均小于L的串
            if num < L:
                cnt_min += 1
            elif cnt_min:
                contiguous_min_lengths.append(cnt_min)
                cnt_min = 0
        if cnt_max:
            max_valid_lengths.append(cnt_max)
        if cnt_min:
            contiguous_min_lengths.append(cnt_min)


        res = 0
        for l in max_valid_lengths:
            res += (1 + l) * l // 2
        for l in contiguous_min_lengths:
            res -= (1 + l) * l // 2
        return res 

