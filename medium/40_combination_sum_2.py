class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [set()] + [set() for i in range(target)]
        for i in candidates:
            for t in range(target, i,-1):
                if t-i > 0:
                    dp[t] |= {s+(i,) for s in dp[t-i]}
            if i <= target:
                dp[i].add((i,)) 

        return map(list, dp[target])
