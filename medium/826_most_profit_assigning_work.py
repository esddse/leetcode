class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_profit = sorted(zip(difficulty, profit), key=lambda item: item[0])
        worker = sorted(worker)

        profit = 0
        idx, p = 0, 0
        for w in worker:
            while idx < len(diff_profit) and diff_profit[idx][0] <= w:
                p = max(p, diff_profit[idx][1])
                idx += 1
            profit += p
        return profit