class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnt = i = 0
        res = []
        for j, c in enumerate(S):
            cnt += 1 if c == "1" else -1
            if cnt == 0:
                res.append("1" + self.makeLargestSpecial(S[i+1:j]) + "0")
                i = j + 1
        return "".join(sorted(res, reverse=True))

