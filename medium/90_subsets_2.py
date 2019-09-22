class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for enum in range(1<<len(nums)):
            s = []
            for i in range(len(nums)):
                if enum>>i&1:
                    s.append(nums[i])
            res.add(tuple(s))
        res = [tuple(s) for s in res]
        return res

