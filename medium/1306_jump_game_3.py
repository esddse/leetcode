from collections import defaultdict
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)
        next_idx = defaultdict(list)
        targets = set()
        for idx, val in enumerate(arr):
            if val == 0:
                targets.add(idx)
            else:
                nxt1, nxt2 = idx + val, idx - val 
                if 0<= nxt1 < size:
                    next_idx[idx].append(nxt1)
                if 0 <= nxt2 < size:
                    next_idx[idx].append(nxt2)

        if start in targets:
            return True

        visited = [False for i in range(size)]
        def dfs(next_idx, visited, start, targets):
            visited[start] = True
            for nxt in next_idx[start]:
                if nxt in targets:
                    return True 
                else:
                    if not visited[nxt]:
                        if dfs(next_idx, visited, nxt, targets):
                            return True 
            return False 
        
        return dfs(next_idx, visited, start, targets)