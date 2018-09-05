class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        s = set([""])
        for i in range(n):
            new_s = set()
            for string in s:
                for j in range(len(string)):
                    new_s.add(string[:j]+"()"+string[j:])
                new_s.add(string+"()")
            s = new_s
        return list(s)

