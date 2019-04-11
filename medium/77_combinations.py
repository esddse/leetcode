class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        def dfs(nums, k):
            if k == 0:
                return [[]]
            res = []
            for i in range(len(nums)):
                rets = dfs(nums[i+1:], k-1)
                for ret in rets:
                    res.append([nums[i]]+ret)
            return res
        return dfs(nums, k)