class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        money5, money10, money20 = 0, 0, 0
        for bill in bills:
            if bill == 5:
                money5 += 1
            elif bill == 10:
                if money5 <= 0:
                    return False
                money10 += 1
                money5 -= 1
            else:
                if money10 >= 1 and money5 >= 1:
                    money10 -= 1
                    money5  -= 1
                elif money5 >= 3:
                    money5 -= 3
                else:
                    return False
                money20 += 1
        return True
            