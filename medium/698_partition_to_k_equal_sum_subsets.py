class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        if size < k:
            return False
        if sum(nums)%k != 0:
            return False
        nums.sort(reverse=True)
        target = [sum(nums)/k] * k

        def dfs(pos):
            if pos == size:
                return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(pos+1):
                        return True
                    target[i] += nums[pos]
            return False
        return dfs(0)
