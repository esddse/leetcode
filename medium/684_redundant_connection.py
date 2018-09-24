class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        parents = [i for i in range(len(edges))]

        def find(i):
            if i != parents[i]:
                parents[i] = find(parents[i])
            return parents[i]

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parents[pj] = parents[pi]

        for a, b in edges:
            pa, pb = find(a-1), find(b-1)
            if pa == pb:
                return [min(a, b), max(a, b)]
            union(a-1, b-1)