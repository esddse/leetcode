class Solution:
    def largestTriangleArea(self, points):
        N = len(points)
        ma = 0
        def calArea(x1, y1, x2, y2, x3, y3):
            return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    ma = max(ma, calArea(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]))
        return ma
