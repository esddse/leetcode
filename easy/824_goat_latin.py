class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = "aeiouAEIOU"

        words = S.split(" ")

        for i in range(len(words)):
            if words[i][0] in vowel:
                words[i] += "ma"
            else:
                words[i] = words[i][1:] + words[i][0] + "ma"
            words[i] += "a" * (i + 1)
        return " ".join(words)
        