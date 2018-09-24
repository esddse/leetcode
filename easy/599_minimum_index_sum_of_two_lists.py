class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        res2idx = {}
        for i, res in enumerate(list1):
            res2idx[res] = i

        minsum = float("inf")
        maxres = []
        for i, res in enumerate(list2):
            if res in res2idx:
                idxsum = i + res2idx[res]
                if idxsum < minsum:
                    minsum = idxsum
                    maxres = [res]
                elif idxsum == minsum:
                    maxres.append(res)
        return maxres