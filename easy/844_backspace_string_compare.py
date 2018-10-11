class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def construct(s):
            res = []
            for c in s:
                if c == "#":
                    if res:
                        res.pop()
                else:
                    res.append(c)
            return "".join(res)
        return construct(S) == construct(T)