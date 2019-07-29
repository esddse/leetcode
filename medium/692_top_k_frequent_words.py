from collections import Counter
import heapq

class Element:
    def __init__(self, cnt, word):
        self.cnt = cnt 
        self.word = word
    def __lt__(self, other):
        if self.cnt == other.cnt:
            return self.word > other.word
        return self.cnt < other.cnt
    def __eq__(self, other):
        return self.cnt == other.cnt and self.word == other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [Element(0,"")] * k
        for k, v in Counter(words).items():
            heapq.heappush(heap, Element(v, k))
            heapq.heappop(heap)
        ret = []
        while heap:
            element = heapq.heappop(heap)
            ret.append(element.word)
        return ret[::-1]