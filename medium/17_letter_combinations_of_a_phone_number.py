class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or "1" in digits:
            return []

        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        s = set(num_to_char[digits[0]])
        for num in digits[1:]:
            new_s = set()
            for seq in s:
                for c in num_to_char[num]:
                    new_s.add(seq+c)
            s = new_s
        return list(s)
