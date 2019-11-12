class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])

        def vector(q1, q2):
            return [q1[0]-q2[0], q1[1]-q2[1]]
        def inner(v1, v2):
            return v1[0]*v2[0] + v1[1]*v2[1]

        v12 = vector(p1, p2)
        v13 = vector(p1, p3)
        v14 = vector(p1, p4)
        len12 = inner(v12, v12)
        len13 = inner(v13, v13)
        len14 = inner(v14, v14)
        if not all([len12, len13, len14]):
            return False
        if inner(v12, v13) == 0 and len12 == len13 and len14 == len12 + len13:
            return True 
        return False