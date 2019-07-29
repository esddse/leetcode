from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = defaultdict(int)
        dp[0] = 1
        for c in coins:
            for a in range(1, amount+1):
                if a >= c:
                    dp[a] += dp[a-c]
        return dp[amount]



