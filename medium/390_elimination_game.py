class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def helper(n, is_left):
            if n == 1:
                return 1
            if is_left:
                return 2*helper(n//2, False)
            else:
                if n%2:
                    return 2*helper(n//2, True)
                else:
                    return 2*helper(n//2, True)-1
        return helper(n, True)