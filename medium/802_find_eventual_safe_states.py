from collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        size = len(graph)
        out_degrees = {i: len(graph[i]) for i in range(size)}
        in_nodes = defaultdict(list)
        for i, lst in enumerate(graph):
            for j in lst:
                in_nodes[j].append(i)
        candidates = {i for i in range(size)}

        res = []
        res_turn = [i for i in out_degrees if out_degrees[i] == 0]
        while res_turn:
            res += res_turn
            for i in res_turn:
                for j in in_nodes[i]:
                    out_degrees[j] -= 1

            candidates -= set(res_turn)
            res_turn = [i for i in out_degrees if out_degrees[i] == 0 and i in candidates]
        res.sort()
        return res
            
