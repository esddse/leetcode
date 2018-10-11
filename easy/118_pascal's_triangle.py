class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        def gen_lst(last_lst):
            lst = [i+j for i, j in zip(last_lst, last_lst[1:])]
            return [1] + lst + [1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        last_lst = [1]
        for i in range(numRows-1):
            lst = gen_lst(last_lst)
            res.append(lst)
            last_lst = lst
        return res