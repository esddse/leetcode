class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        board = [[False for i in range(length)] for j in range(length)]
        c_position = {}

        cnt = 0
        for i, c in enumerate(s):
            board[i][i] = True
            cnt += 1

            if c not in c_position:
                c_position[c] = [i]
                continue
            
            for p in c_position[c]:
                inner_start = p + 1
                inner_end   = i - 1
                if board[inner_start][inner_end] or i-p == 1:
                    board[p][i] = True
                    cnt += 1

            c_position[c].append(i)

        return cnt

