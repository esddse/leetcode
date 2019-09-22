class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N

        num_digits = []
        while N:
            num_digits.append(N%10)
            N //= 10
        num_digits.reverse()
        size = len(num_digits)

        # find decease idx
        i = 1
        while i < size and num_digits[i-1] <= num_digits[i]:
            i += 1

        if i == size:
            return int("".join(map(str, num_digits)))
        else:
            j = i-1
            numj = num_digits[j]
            while j >= 0 and num_digits[j] == numj:
                j -= 1
            j += 1
            new_digits = num_digits[:j]+[num_digits[j]-1]+[9] * (size-j-1)
            return int("".join(map(str, new_digits)))
