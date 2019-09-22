class Solution:
    def knightDialer(self, N: int) -> int:
        
        modulo = 1e9+7
        prev_num = {0:[4,6],   1:[6, 8],  2:[7, 9],
                    3:[4,8],   4:[3,9,0], 5:[],
                    6:[1,7,0], 7:[2,6],   8:[1,3], 9:[2,4]}


        dp = {i:1 for i in range(10)}
        for i in range(2, N+1):
            new_dp = {i:0 for i in range(10)}
            for i in range(10):
                for prev in prev_num[i]:
                    new_dp[i] = (new_dp[i] + dp[prev]) % modulo
            dp = new_dp

        return int(sum([num for num in dp.values()]) % modulo)