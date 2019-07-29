

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        size = len(stones)

        min_moves = float("inf")
        max_moves = 0

        i = 0
        for j in range(size):
            while stones[j] - stones[i] >= size:
                i += 1
            if j - i + 1 == size - 1 and stones[j] - stones[i] == size - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, size - (j - i + 1))

        max_moves = (stones[-1]-stones[0]+1)-size-min(stones[1]-stones[0]-1, stones[-1]-stones[-2]-1)

        return [min_moves, max_moves]