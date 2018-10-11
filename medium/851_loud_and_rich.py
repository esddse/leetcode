class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        N = len(quiet)
        rsets = [set([i]) for i in range(len(N))]

        for x, y in richer:
