class Solution:
    def freqAlphabets(self, s: str) -> str:
        if not s:
            return ""
        size = len(s)
        i, ans = 0, ""
        while i < size:
            if i + 2 < size and s[i+2] == "#":
                ans += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                ans += chr(int(s[i])+96)
                i += 1
        return ans