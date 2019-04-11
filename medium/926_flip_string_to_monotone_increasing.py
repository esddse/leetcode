class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        
        before_zeros = []
        cnt = 0
        for s in S:
            if s == '1':
                cnt += 1
            before_zeros.append(cnt)

        after_ones = []
        cnt = 0
        for s in S[::-1]:
            if s == '0':
                cnt += 1
            after_ones.append(cnt)
        after_ones.reverse()

        min_cnt = min(after_ones[0], before_zeros[-1])
        for i in range(len(S)-1):
            if min_cnt > before_zeros[i] + after_ones[i+1]:
                min_cnt = before_zeros[i] + after_ones[i+1]
        return min_cnt