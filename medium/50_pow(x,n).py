class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        d = {}
        def mypow(x, n, d):
            if n in d:
                return d[n]
            else:
                if n == 0:
                    ans = 1 
                elif n == 1:
                    ans = x 
                elif n == -1:
                    ans = 1/x
                else:
                    if n % 2 == 0:
                        ans = mypow(x, n/2, d) * mypow(x, n/2, d)
                    else:
                        if n > 0:
                            ans = mypow(x, (n-1)/2, d) * mypow(x, (n-1)/2, d) * x
                        else:
                            ans = mypow(x, (n+1)/2, d) * mypow(x, (n+1)/2, d) * 1/x

                d[n] = ans
                return ans
        return mypow(x, n, d)