import heapq
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(s)
        parents = [i for i in range(size)]

        def find(a):
            if parents[a] == a:
                return a
            parents[a] = find(parents[a])
            return parents[a]

        def merge(a, b):
            pa, pb = find(a), find(b)
            parents[pa] = pb

        # set union
        for a, b in pairs:
            merge(a, b)
        # assign to heap
        sets = defaultdict(list)
        for i in range(size):
            sets[find(i)].append(s[i])
        for i in sets:
            heapq.heapify(sets[i])
        # regenerate str
        news = ""
        for i in range(size):
            news += heapq.heappop(sets[parents[i]])
        return news

