

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)

        cnt = 0
        for i in range(size-2):
            for j in range(i+1, size-1):
                ab = nums[i] + nums[j]
                l, r = j, size
                while l < r:
                    m1 = (l + r) // 2
                    m2 = m1 + 1
                    c1 = nums[m1]
                    c2 = nums[m2] if m2 < size else float("inf")
                    # print(l, r, m1, m2, c1, c2)
                    if ab <= c1:
                        r = m1
                    elif ab > c2:
                        l = m2
                    else:
                        cnt += m1 - j
                        # print(cnt)
                        break

        return cnt