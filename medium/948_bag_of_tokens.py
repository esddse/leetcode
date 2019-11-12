class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens)-1
        res, cnt = 0, 0
        while i <= j:
            if P >= tokens[i]:
                cnt += 1
                P -= tokens[i]
                i += 1
            else:
                if cnt:
                    cnt -= 1
                    P += tokens[j]
                    j -= 1
                else:
                    break
            res = max(res, cnt)
        return res
