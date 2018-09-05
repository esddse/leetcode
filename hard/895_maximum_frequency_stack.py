
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq  = defaultdict(int)
        self.stack = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.freq[x] += 1
        self.stack[self.freq[x]].append(x)
        self.max_freq = max(self.max_freq, self.freq[x])

        
    def pop(self):
        """
        :rtype: int
        """
        x = self.stack[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.stack[self.max_freq]:
            self.max_freq -= 1
        return x



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()