class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda item: item[0])
        out = []
        start, end = None, None
        for interval in intervals:
            if start is None:
                start, end = interval
            else:
                if interval[0] <= end:
                    start = min(start, interval[0])
                    end   = max(end, interval[1])
                else:
                    out.append([start, end])
                    start, end = interval
        if start is not None:
            out.append([start, end])
        return out