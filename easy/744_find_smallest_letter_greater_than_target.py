class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        res = ""
        target = ord(target)
        min_num = float("inf")
        for letter in letters:
            num = (ord(letter) - target) % 26
            if num and num < min_num:
                min_num = num
                res = letter 
        return res