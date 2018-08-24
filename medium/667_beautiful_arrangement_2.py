class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        i, j = 1, k+1
        pre = []
        while i <= j:
            if i == j:
                pre.append(i)
            else:
                pre += [i, j]
            i += 1
            j -= 1
        post = [i for i in range(k+2, n+1)]
        return pre + post