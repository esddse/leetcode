from functools import reduce
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        for i in range(len(values)):
            a, b = equations[i]
            v = values[i]
            if a not in d:
                d[a] = {b:v}
            else:
                d[a][b] = v
            if b not in d:
                d[b] = {a:1/v}
            else:
                d[b][a] = 1/v
        rets = []

        def dfs(current, target, marks, vals):
            for v in d[current]:
                if v in marks:
                    continue
                if v == target:
                    vals.append(d[current][v])
                    return True 
                marks.add(v)
                vals.append(d[current][v])
                find = dfs(v, target, marks, vals)
                if find:
                    return True
                else:
                    vals.pop()
            return False

        for a, b in queries:
            if a not in d or b not in d:
                rets.append(-1.)
                continue
            if a == b:
                rets.append(1.)
                continue
            vals = [] 
            find = dfs(a, b, set([a]), vals)
            if find:
                rets.append(reduce(lambda x,y: x*y, vals))
            else:
                rets.append(-1.)
        return rets
                
            
