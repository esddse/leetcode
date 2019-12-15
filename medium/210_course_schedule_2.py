class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ret = []
        # init
        numPre = {i: 0 for i in range(numCourses)}
        nextCourse = {i: set() for i in range(numCourses)}
        for c, p in prerequisites:
            nextCourse[p].add(c)
            numPre[c] += 1

        while numPre:
            to_del = []
            for c, num in numPre.items():
                if num == 0:
                    ret.append(c)
                    for nc in nextCourse[c]:
                        numPre[nc] -= 1
                    to_del.append(c)
            if not to_del:
                return []
            for c in to_del:
                del numPre[c]
        return ret


