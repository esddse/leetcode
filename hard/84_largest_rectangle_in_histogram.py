class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        size = len(heights)

        lefts = [i for i in range(size)]
        for i in range(size):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = lefts[p]
            lefts[i] = p

        rights = [i for i in range(size)]
        for i in range(size-1, -1, -1):
            p = i + 1
            while p < size and heights[p] >= heights[i]:
                p = rights[p]
            rights[i] = p 

        max_area = 0
        for i, h in enumerate(heights):
            l, r = lefts[i], rights[i]
            max_area = max(max_area, heights[i] * (r-l-1))
        return max_area