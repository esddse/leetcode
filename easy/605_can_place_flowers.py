class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if not flowerbed[i] and (i == 0 or not flowerbed[i-1]) and (i == len(flowerbed)-1 or not flowerbed[i+1]):
                n -= 1
                flowerbed[i] = 1
        return n <= 0