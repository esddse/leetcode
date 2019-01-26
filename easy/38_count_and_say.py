class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        string = "1"

        def gen_next(string):
            new_str = ""
            frac = ""
            for c in string:
                if frac and c != frac[-1]:
                    new_str += str(len(frac)) + frac[0]
                    frac = ""
                frac += c
            new_str += str(len(frac)) + frac[0]
            return new_str

        while n - 1:
            string = gen_next(string)
            n -= 1

        return string