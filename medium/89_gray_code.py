class Solution:
    def grayCode(self, n: int) -> List[int]:
        ret = [0]
        for i in range(n):
            new = []
            for j in ret[::-1]:
                new.append(j | 1 << i)
            ret += new 
        return ret
