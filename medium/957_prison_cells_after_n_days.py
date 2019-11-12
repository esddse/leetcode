class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0:
            return cells
        size = len(cells)
        mask = (1<<(size-1))-2
        # create init cell
        cell = 0
        for c in cells:
            cell <<= 1
            cell += c
        # update
        def update(cell, size, mask):
            cell_l = cell >> 1
            cell_r = cell << 1
            cell = ~ (cell_l^cell_r)
            cell &= mask
            return cell

        d, r = {}, {}
        step = 0
        N -= 1
        while step <= N:
            cell = update(cell, size, mask)
            if cell in d:
                break
            d[cell] = step 
            r[step] = cell
            step += 1

        cell = r[N%len(r)]
        ret = []
        for i in range(size):
            ret = [(cell>>i)&1] + ret

        return ret