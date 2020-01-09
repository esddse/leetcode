class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        len_low, len_high = len(str(low)), len(str(high))
        ret = []
        for l in range(len_low, len_high+1):
            for start in range(1, 11-l):
                num = int("".join([str(start+i) for i in range(l)]))
                if low <= num <= high:
                    ret.append(num)
        return ret
