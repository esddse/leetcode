class Solution:
    def integerReplacement(self, n: int) -> int:
        self.min_replace = float("inf")
        def replace(num, step):
            if step >= self.min_replace:
                return self.min_replace
            if num == 1:
                self.min_replace = step
                return self.min_replace
            if num&1:
                return min(replace(num+1, step+1), replace(num-1, step+1))
            else:
                return replace(num>>1, step+1)
        return replace(n, 0)