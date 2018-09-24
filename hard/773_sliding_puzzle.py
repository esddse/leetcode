class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        moves = {0:{1,3}, 1:{0,2,4}, 2:{1,5}, 3:{0,4}, 4:{1,3,5}, 5:{2,4}}
        used  = set()
        cnt   = 0

        init_s = "".join([str(c) for c in board[0]+board[1]])
        queue  = [(init_s, init_s.index("0"))]
        while queue:
            new_queue = []
            for s, i in queue:
                if s == "123450":
                    return cnt
                used.add(s)
                for move in moves[i]:
                    new_s = [c for c in s]
                    new_s[i], new_s[move] = new_s[move], new_s[i]
                    new_s = "".join(new_s)
                    if new_s not in used:
                        new_queue.append((new_s, move))
            cnt += 1
            queue = new_queue
        return -1
        