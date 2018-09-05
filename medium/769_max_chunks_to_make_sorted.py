class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        mark = [0] * (len(arr)+1)

        def find_next(mark, i):
            while i < len(mark) and mark[i]:
                i += 1
            return i

        next_num = 0
        cnt = 0
        for i in range(len(arr)):
            num = arr[i]
            mark[num] = 1
            if num == next_num:
                next_num = find_next(mark, next_num)
                if next_num-1 == i:
                    cnt += 1
        return cnt
        