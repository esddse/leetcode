class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(candidates, target, path, res):
            if target == 0:
                res.append(path)
                return
            for i, cand in enumerate(candidates):
                if cand > target: continue
                dfs(candidates[i:], target-cand, path+[cand], res)
        dfs(candidates, target, [], res)
        return res
