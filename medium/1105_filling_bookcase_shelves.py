class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        size = len(books)
        dp = [0 for i in range(size)]
        dp[0] = books[0][1]

        for i in range(1, size):
            dp[i] = dp[i-1] + books[i][1]
            w, h = books[i][0], books[i][1]
            for j in range(i-1, -1, -1):
                w += books[j][0]
                h = max(h, books[j][1])
                if w > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j-1] + h)
        return dp[size-1]