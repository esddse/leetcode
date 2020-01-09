class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums)-1
        queue = [(0, nums[0])]
        nums[0] = -1
        step = 0
        while queue:
            new_queue = []
            max_i = 0
            for idx, jump in queue:               
                if idx == target:
                    return step
                for i in range(max(idx+1, max_i), min(idx+jump, target)+1):
                    if nums[i] >= 0:
                        new_queue.append((i, nums[i]))
                        nums[i] = -1
                max_i = min(idx+jump, target)
            queue = new_queue
            step += 1