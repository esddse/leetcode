# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def gen_trees(lst):
            if not lst:
                return [None] 
            trees = []
            for i in range(len(lst)):
                tree = TreeNode(lst[i])
                for left in gen_trees(lst[:i]):
                    for right in gen_trees(lst[i+1:]):
                        tree.left = left 
                        tree.right = right 
                        trees.append(copy.deepcopy(tree))
            return trees

        return gen_trees(list(range(1, n+1)))
        