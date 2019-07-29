# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        def get_struct(node):
            if not node:
                return "null"
            struct = "%s,%s,%s" % (str(node.val), get_struct(node.left), get_struct(node.right))
            d[struct].append(node)
            return struct
        d = defaultdict(list)
        get_struct(root)
        ret = [d[struct][0] for struct in d if len(d[struct]) > 1]
        return ret

