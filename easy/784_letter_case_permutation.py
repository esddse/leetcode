class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [""]

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet += alphabet.upper()
        
        strings = []
        if S[0] in alphabet:
            strings = [S[0].lower(), S[0].upper()]
        else:
            strings = [S[0]]

        for s in S[1:]:
            if s in alphabet:
                strings_l = [string + s.lower() for string in strings]
                strings_u = [string + s.upper() for string in strings]
                strings = strings_l + strings_u
            else:
                strings = [string + s for string in strings]
        return strings
 