class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        groups = []
        start_idx = 0
        last = None
        for i, c in enumerate(S):
            if c != last:
                last = c
                if i and i - start_idx >= 3:
                    groups.append([start_idx, i-1])
                start_idx = i
        if i and i - start_idx >= 2:
            groups.append([start_idx, i])
        return groups