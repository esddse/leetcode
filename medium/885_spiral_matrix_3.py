class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        p_dir = 0
        x, y = r0, c0
        stride = 1
        outputs = [[x, y]]

        while True:
            for __ in range(2):
                for i in range(stride):
                    x += direction[p_dir][0]
                    y += direction[p_dir][1]
                    if x >= 0 and x < R and y >= 0 and y < C:
                        outputs.append([x, y])
                p_dir = (p_dir + 1) % 4
            stride += 1
            if len(outputs) == R * C:
                break

        return outputs

