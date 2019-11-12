class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        swaped = set([num])
        for i in range(len(num_str)):
            for j in range(i+1, len(num_str)):
                new_num = num_str[:i] + num_str[j] + num_str[i+1:j] + num_str[i] + num_str[j+1:]
                swaped.add(int(new_num))
        return max(swaped)