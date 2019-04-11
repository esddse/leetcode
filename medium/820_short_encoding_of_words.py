class Node(object):
    def __init__(self, is_start=False):
        self.next = {}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Node()
        cnt = 0
        for word in words:
            r_word = word[::-1]
            node = root
            for i, c in enumerate(r_word):
                if c not in node.next:
                    if not node.next: # leaf
                        cnt += 1
                    else:
                        cnt += i+1+1
                    node.next[c] = Node()
                node = node.next[c]
        return cnt+1
