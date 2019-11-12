class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt, ret = 0, 0
        for c in s:
            if c == "L":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ret += 1
        return ret