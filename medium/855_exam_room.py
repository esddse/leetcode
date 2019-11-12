import bisect

class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.seated = []

    def seat(self) -> int:
        if not self.seated:
            self.seated.append(0)
            return 0
        else:
            max_dist, max_pos = 0, 0
            for i in range(len(self.seated)):
                # 头
                if i == 0:
                    dist = self.seated[0]
                    if dist >= 1 and dist > max_dist:
                        max_dist = dist
                        max_pos = 0
                else:
                    dist = (self.seated[i-1] + self.seated[i]) // 2 - self.seated[i-1]
                    if dist >= 1 and dist > max_dist:
                        max_dist = dist 
                        max_pos = (self.seated[i-1] + self.seated[i]) // 2
            # 尾
            dist = self.N-1  - self.seated[-1]
            if dist >= 1 and dist > max_dist:
                max_dist = dist 
                max_pos = self.N-1
            idx = bisect.bisect_left(self.seated, max_pos)
            self.seated.insert(idx, max_pos)
            return max_pos

    def leave(self, p: int) -> None:
        idx = bisect.bisect_left(self.seated, p)
        self.seated.pop(idx)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)