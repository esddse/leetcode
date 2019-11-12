class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        size = len(triangle)
        if size < 1:
            return 
        for l in range(size-2, -1, -1):
            for i in range(len(triangle[l])):
                triangle[l][i] += min(triangle[l+1][i], triangle[l+1][i+1])
        return triangle[0][0]
        