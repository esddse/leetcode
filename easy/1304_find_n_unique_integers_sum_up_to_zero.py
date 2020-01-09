class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        if n % 2 == 0:
            for i in range(n//2):
                ret.append(-(i+1))
                ret.append(i+1)
        else:
            ret.append(0)
            for i in range((n-1)//2):
                ret.append(-(i+1))
                ret.append(i+1)
        return ret
        