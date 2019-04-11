class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0
        obstacles = set([(x,y) for x, y in obstacles])
        ret = 0
        for c in commands:
            if c == -2:
                d = (d - 1) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                while c:
                    dx, dy = directions[d]
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
                    c -= 1
            ret = max(ret, x*x + y*y)
        return ret