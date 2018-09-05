class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """

        places = {x:i for i, x in enumerate(row)}
        cnt = 0
        for i in range(0,len(row),2):
            y = row[i] ^ 1
            if row[i+1] != y:
                j = places[y]
                row[j] = row[i+1]
                places[row[j]] = j
                cnt += 1
        return cnt
