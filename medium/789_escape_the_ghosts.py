class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        you_len = manhattan([0,0], target)

        for ghost in ghosts:
            ghost_len = manhattan(ghost, target)
            if ghost_len <= you_len:
                return False
        return True