class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)

        q = 0
        while dividend >= divisor:
            c = 0
            while (divisor<<c) <= dividend:
                c += 1
            c -= 1
            q += (1 << c)
            dividend -= (divisor << c)
        q = q * sign
        q = -(1<<31) if q < -(1<<31) else q
        q = (1<<31)-1 if q > (1<<31)-1 else q
        return q