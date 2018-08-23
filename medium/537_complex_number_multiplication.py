class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        def split_number(num):
            num = num.strip().split("+")
            r = int(num[0])
            i = int(num[1][:-1])
            return r, i

        ar, ai = split_number(a)
        br, bi = split_number(b)

        r = ar * br - ai * bi
        i = ar * bi + ai * br
        return str(r) + "+" + str(i) + "i"