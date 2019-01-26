class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = list(zip(*[list(s) for s in strs]))
        common = ""
        for i in range(len(strs)):
            if len(set(strs[i])) > 1:
                break
            common += strs[i][0]
        return common