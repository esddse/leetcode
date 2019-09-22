class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        a2n = {a: i for i, a in enumerate(alphabet)}
        n2a = {n: a for a, n in a2n.items()}

        total_shifts = sum(shifts)
        newS = []
        for i in range(len(S)):
            s = S[i]
            s = n2a[(a2n[s]+total_shifts)%26]
            newS.append(s)
            total_shifts -= shifts[i]

        return "".join(newS)