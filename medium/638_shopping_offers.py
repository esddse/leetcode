class Solution:
    def shoppingOffers(self, prices, special, needs):
        """
        :type prices: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        d = {}
        def dfs(needs):
            val = sum([prices[i] * needs[i] for i in range(len(needs))])
            for sp in special:
                price = sp[-1] 
                goods = sp[:-1]
                tmp = tuple(needs[i] - goods[i] for i in range(len(needs)))
                if all([item >= 0 for item in tmp]):
                    val = min(val, d.get(tmp, dfs(tmp)) + price)
                if tmp not in d:
                    d[tmp] = val
            return val
        return dfs(needs)
