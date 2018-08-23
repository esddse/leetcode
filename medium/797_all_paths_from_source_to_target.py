class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        from collections import deque
        
        target = len(graph) - 1
        paths = []
        q = deque()
        q.append([0])

        while len(q) > 0:
            path = q.popleft()
            nodes = graph[path[-1]]
            for node in nodes:
                if node == target:
                    paths.append(path+[node])
                else:
                    q.append(path+[node])

        return paths 