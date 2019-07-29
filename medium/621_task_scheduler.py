from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = list(Counter(tasks).values())
        m = max(counter)
        mct = counter.count(m)
        return max(len(tasks), (m-1)*(n+1)+mct)