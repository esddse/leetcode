class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = [(start, end) for start, end in clips]
        clips.sort()

        c_start, c_end = -1, 0
        best_start, best_end = -1, 0
        cnt = 0
        for start, end in clips:
            # print(start, end)
            if start > c_end:
                if best_end <= start and best_end < T:
                    return -1
                else:
                    c_start = best_start
                    c_end   = best_end
                    cnt += 1
                    if c_end >= T:
                        return cnt
            if end > best_end:
                best_start = start
                best_end   = end
                # print("best:", best_start, best_end)
        if best_end <= c_end and best_end < T:
            return -1
        else:
            c_start = best_start
            c_end   = best_end
            cnt += 1
        if c_end < T:
            return -1
        return cnt 

