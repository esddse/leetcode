class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        len_row = len(image)
        len_col = len(image[0])

        mark = [[False] * len_col for _ in range(len_row)]
        oldColor = image[sr][sc]

        queue = [(sr, sc)]
        while queue:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            new_queue = []
            for x, y in queue:
                image[x][y] = newColor
                mark[x][y] = True
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy 
                    if nx >= 0 and nx < len_row and ny >= 0 and ny < len_col and \
                       image[nx][ny] == oldColor and not mark[nx][ny]:
                       new_queue.append((nx, ny))
            queue = new_queue
        return image