# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        queue = [root]
        ret = []
        left = 1
        while queue:
            new_queue = []
            res = []
            for node in queue[::-1]:
                res.append(node.val)
                if left == 1:
                    if node.left:
                        new_queue.append(node.left)
                    if node.right:
                        new_queue.append(node.right)
                else:
                    if node.right:
                        new_queue.append(node.right)
                    if node.left:
                        new_queue.append(node.left)

            ret.append(res)
            queue = new_queue
            left *= -1

        return ret