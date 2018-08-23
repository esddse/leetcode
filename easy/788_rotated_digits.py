class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid = "2569"
        unchange = "018"
        cnt = 0
        for num in range(1, N+1):
            flag = False
            funchange = True
            for digit in str(num):
                if digit in valid:
                    flag = True
                    continue
                if digit not in valid and digit not in unchange:
                    funchange = False
                    break
            if flag and funchange:
                cnt += 1
        return cnt