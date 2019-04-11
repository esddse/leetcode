# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
          
        adj = defaultdict(list)
        def dfs(node, adj):
            val = node.val 
            if node.left:
                adj[val].append(node.left.val)
                adj[node.left.val].append(val)
                dfs(node.left, adj)
            if node.right:
                adj[val].append(node.right.val)
                adj[node.right.val].append(val)
                dfs(node.right, adj)
        dfs(root, adj)

        queue = [target.val]
        mark = set(queue)
        while queue and K:
            new_queue = set()
            for val in queue:
                new_queue.update(adj[val])
            K -= 1
            queue = new_queue - mark 
            mark |= queue 
        return list(queue)

