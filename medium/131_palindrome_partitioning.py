class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s = tuple(s)
        res, queue = set(), set()
        res.add(s)
        queue.add(s)
        while queue:
            new_queue = set()
            for s in queue:
                for i in range(len(s)):
                    if 0<i<len(s)-1:
                        if s[i-1] == s[i+1][::-1]:
                            new_s = s[:i-1] + (s[i-1]+s[i]+s[i+1],) + s[i+2:]
                            res.add(new_s)
                            new_queue.add(new_s)
                    if 0<i:
                        if s[i-1] == s[i][::-1]:
                            new_s = s[:i-1] + (s[i-1]+s[i],) + s[i+1:]
                            res.add(new_s)
                            new_queue.add(new_s)
            queue = new_queue
        return list(map(list, res))