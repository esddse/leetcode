class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if numRows == 1:
            return s
        size = len(s)
        i = 0
        zigzag = []
        while s:
            if i == 0:
                col = list(s[:numRows])
                col += [""] * (numRows-len(col))
                s = s[numRows:]
            else:
                col = [""] * (numRows-i-1)+[s[0]]+[""]*i
                s = s[1:]
            zigzag.append(col)
            i = (i+1)%(numRows-1)
        ret = ""
        for row in zip(*zigzag):
            for c in row:
                if c:
                    ret += c
        return ret 
