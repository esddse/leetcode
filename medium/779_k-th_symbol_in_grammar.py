class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        K = K-1
        ret = 0
        for i in range(30):
            ret ^= (K>>i)&1
        return ret