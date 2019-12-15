class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        size = len(s)
        diff = [abs(ord(s[i])-ord(t[i])) for i in range(size)]
        max_len, cost = 0, 0
        start, end = 0, 0
        while end < size:
            while end < size and cost+diff[end] <= maxCost:
                cost += diff[end]
                end += 1
            max_len = max(max_len, end-start)
            cost -= diff[start]
            start += 1
            if end < start:
                end, cost = start, 0
        return max_len

