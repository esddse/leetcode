from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        disset = defaultdict(set)
        for i, j in dislikes:
            disset[i-1].add(j-1)
            disset[j-1].add(i-1)

        parent = [i for i in range(N)]

        def find(idx):
            if parent[idx] == idx:
                return idx
            parent[idx] = find(parent[idx])
            return parent[idx]

        def merge(idx1, idx2):
            parent1, parent2 = find(idx1), find(idx2)
            parent[parent1] = parent2

        for i, s in disset.items():
            s = list(s)
            for j in s:
                if j != s[0]:
                    merge(j, s[0])
                if find(i) == find(j):
                    return False
        return True