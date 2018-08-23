class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        def gen_distance(start, end, state=None):
            if state == 0:
                return [i for i in range(end+1)][::-1]
            elif state == 1:
                return [i+1 for i in range(end-start)]
            else:
                return [min(i-start+1, end-i) for i in range(start, end+1)]

        p = 0
        distances = []
        for i in range(len(S)):
            if S[i] == C:
                if p == 0:
                    distances += gen_distance(p, i, state=0)
                else:
                    distances += gen_distance(p, i)
                p = i + 1
        distances += gen_distance(p, len(S), state=1)
        return distances