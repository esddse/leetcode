class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        rets = set()
        def permute(curr, rest):
            if not rest:
                rets.add(tuple(curr))
            for i, num in enumerate(rest):
                permute(curr+[num], rest[:i]+rest[i+1:])
        permute([], nums)
        rets = list([list(item) for item in rets])
        return rets

