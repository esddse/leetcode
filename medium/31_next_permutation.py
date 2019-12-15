class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        size = len(nums)
        find = False
        max_num = nums[-1]
        for i in range(size-2, -1, -1):
            if nums[i] > max_num:
                max_num = nums[i]
            elif nums[i] < max_num:
                # find min num > num[i]
                min_num, min_j = float("inf"), None
                for j in range(i+1, size):
                    if nums[j] > nums[i] and nums[j] < min_num:
                        min_num = nums[j]
                        min_j = j
                nums[i], nums[min_j] = nums[min_j], nums[i]
                for end in range(size-1, i, -1):
                    for p in range(i+1, end):
                        if nums[p] > nums[p+1]:
                            nums[p], nums[p+1] = nums[p+1], nums[p]
                find = True
                break
        if not find:
            nums.sort()
