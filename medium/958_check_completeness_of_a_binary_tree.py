# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = [root]
        last_row = False
        while queue:
            print([node.val for node in queue])
            new_queue = []
            has_none = False
            for node in queue:
                if has_none:
                    if node.left or node.right:
                        return False
                else:
                    if node.left:
                        new_queue.append(node.left)
                        if node.right:
                            new_queue.append(node.right)
                        else:
                            has_none = True 
                    else:
                        has_none = True 
                        if node.right:
                            return False
            if last_row:
                return not new_queue
            if has_none:
                last_row = True
            queue = new_queue
        return True


