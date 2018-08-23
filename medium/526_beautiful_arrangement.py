class Solution(object):

    def valid_position(self, num, N):
        valid_pos = []
        for pos in range(N):
            pos += 1
            if num / pos == num // pos:
                valid_pos.append(pos)
            elif pos / num == pos // num:
                valid_pos.append(pos)
        return valid_pos

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        valid_pos = {}
        for num in range(N):
            num += 1
            valid_pos[num] = self.valid_position(num, N)

        self.cnt = 0
        
        def search(current, stack):
            for pos in valid_pos[current]:
                if pos not in stack:
                    if current == N:
                        self.cnt += 1
                    else:
                        stack.append(pos)
                        search(current+1, stack)
                        stack.pop()
        search(1, [])
        return self.cnt



        