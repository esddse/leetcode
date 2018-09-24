class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cntA = 0
        countinousL = 0
    
        for c in s:
            if c == 'A':
                countinousL = 0
                cntA += 1
                if cntA > 1:
                    return False
            elif c == 'L':
                countinousL += 1
                if countinousL > 2:
                    return False
            else:
                countinousL = 0
        return True