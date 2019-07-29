class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        size = len(points)
        p_set = set([(i, j) for i, j in points])

        def vec(p1, p2):
            return (p2[0]-p1[0], p2[1]-p1[1])

        def add(p, v):
            return (p[0]+v[0], p[1]+v[1])

        def sub(p, v):
            return (p[0]-v[0], p[1]-v[1])

        def inner_product(v1, v2):
            return v1[0]*v2[0] + v1[1]*v2[1]

        def predict_right_angle(p1, p2, p3):
            p1p2, p1p3, p2p3 = vec(p1, p2), vec(p1, p3), vec(p2, p3)
            if inner_product(p1p2, p1p3) == 0:
                return add(p2, p1p3), p1p2, p1p3
            if inner_product(p1p2, p2p3) == 0:
                return add(p1, p2p3), p1p2, p2p3
            if inner_product(p1p3, p2p3) == 0:
                return sub(p2, p1p3), p1p3, p2p3
            return None

        def area(v1, v2):
            e1 = (v1[0]**2 + v1[1]**2) ** 0.5
            e2 = (v2[0]**2 + v2[1]**2) ** 0.5
            return e1 * e2


        min_area = float("inf")
        for i in range(size):
            p1 = points[i]
            for j in range(i+1, size):
                p2 = points[j]
                for k in range(j+1, size):
                    p3 = points[k]
                    p4 = predict_right_angle(p1, p2, p3)
                    if p4:
                        p4, v1, v2 = p4
                        if p4 in p_set:
                            min_area = min(min_area, area(v1, v2))
        if min_area != float("inf"):
            return min_area
        else:
            return 0