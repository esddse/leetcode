class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = list(reversed(list(a)))
        b = list(reversed(list(b)))
        max_len = max(len(a), len(b))
        a += ["0"] * (max_len - len(a))
        b += ["0"] * (max_len - len(b))

        res = []
        carry = 0
        for i in range(max_len):
            ai, bi = a[i], b[i]
            s = int(ai) + int(bi) + carry
            carry = s // 2
            res.append(str(s % 2))
        if carry:
            res.append(str(carry))
        return "".join(reversed(res))

