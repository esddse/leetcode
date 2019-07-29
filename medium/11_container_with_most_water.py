class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, (right - left) * height[left])
                left += 1
            else:
                max_area = max(max_area, (right - left) * height[right])
                right -= 1
        return max_area
