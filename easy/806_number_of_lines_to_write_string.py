class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        len_letters = [widths[ord(s)-97] for s in S]
        len_lines = [0]

        for l in len_letters:
            if l + len_lines[-1] <= 100:
                len_lines[-1] += l
            else:
                len_lines.append(l)

        return len(len_lines), len_lines[-1]