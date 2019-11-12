class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_insert, p_select = 0, 0
        cnt, last = 0, None
        while p_select < len(nums):
            num = nums[p_select]
            if num != last:
                cnt = 1
                last = num
                nums[p_insert] = nums[p_select]
                p_insert += 1
            else:
                cnt += 1
                if cnt <= 2:
                    nums[p_insert] = nums[p_select]
                    p_insert += 1
            p_select += 1
        return p_insert
