from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_dict  = defaultdict(list)
        in_degree = [0] * numCourses 
        for course, pre in prerequisites:
            pre_dict[course].append(pre)
            in_degree[pre] += 1

        s = {i for i in range(numCourses)}

        while True:
            d = set()
            to_loop = False
            for c in s:
                if in_degree[c] <= 0:
                    to_loop = True
                    d.add(c)
                    for pre in pre_dict[c]:
                        in_degree[pre] -= 1
            s -= d
            if not to_loop:
                break

        return len(s) == 0
