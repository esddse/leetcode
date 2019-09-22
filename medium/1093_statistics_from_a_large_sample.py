class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        maximum = 0
        minimum = float("inf")
        mean, mean_cnt = 0, 0
        mode, mode_cnt = 0, 0
        for num, cnt in enumerate(count):
            if cnt:
                maximum = max(maximum, num)
                minimum = min(minimum, num)
                mean += num * cnt 
                mean_cnt += cnt
                if cnt > mode_cnt:
                    mode = num
                    mode_cnt = cnt
        middle_idx = [mean_cnt//2, mean_cnt//2+1] if mean_cnt % 2 == 0 else [mean_cnt//2+1]
        median, already = 0, 0
        for num, cnt in enumerate(count):
            for idx in middle_idx:
                if already<idx<=already+cnt:
                    median += num
            already += cnt 
        median /= len(middle_idx)
        return float(minimum), float(maximum), mean/mean_cnt, median, float(mode)