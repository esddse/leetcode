class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        row = [1] * (rowIndex + 1)
        for k in range(rowIndex):
            l2, l1 = row[0], row[1]
            for i in range(1, k+1):
                row[i] = l1 + l2
                l2, l1 = l1, row[i+1]
        return row