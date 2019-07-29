class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(num, ret):
            if num <= n:
                ret.append(num)
                num *= 10
                if num <= n:
                    for i in range(10):
                        dfs(num+i, ret)

        ret = []
        for i in range(1, 10):
            dfs(i, ret)
        return ret