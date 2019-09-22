class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda item: (item[1], item[0]))

        cnt = 0
        curr_right = -float("inf")
        for left, right in intervals:
            if left < curr_right:
                cnt += 1
            else:
                curr_right = right
        return cnt