class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)
        rights = sorted([r for l, r in intervals])
        lefts  = sorted([(item[0], i) for i, item in enumerate(intervals)])

        right2left = {}
        i, j = 0, 0
        while i < size:
            if rights[i] not in right2left:
                right2left[rights[i]] = -1
            if j < size:
                if rights[i] <= lefts[j][0]:
                    right2left[rights[i]] = lefts[j][1]
                    i += 1
                else:
                    j += 1
            else:
                i += 1

        res = [right2left[r] for l, r in intervals]
        return res
