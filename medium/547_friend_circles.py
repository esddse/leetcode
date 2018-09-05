
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        def find(fathers, i):
            rank = 0
            while fathers[i] != i:
                fathers[i] = fathers[fathers[i]]
                i = fathers[i]
                rank += 1
            return fathers[i], rank

        def union(fathers, i, j):
            father_i, rank_i = find(fathers, i)
            father_j, rank_j = find(fathers, j)
            if father_i != father_j:
                if rank_i < rank_j:
                    fathers[father_i] = father_j
                else:
                    fathers[father_j] = father_i


        fathers = [i for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M)):
                if i != j and M[i][j]:
                    union(fathers, i, j)

        circles = []
        for i in range(len(M)):
            father, __ = find(fathers, i)
            if father not in circles:
                circles.append(father)
        return len(circles)