# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        def construct(pre, post):

            if not pre:
                return None

            val = pre[0]
            node = TreeNode(val)

            if len(pre) == 1:
                return node

            child = pre[1]
            idx_child_post = post.index(child)
            child = post[-2]
            idx_child_pre = pre.index(child)

            pre_left  = pre[1:idx_child_pre]
            pre_right = pre[idx_child_pre:]

            post_left  = post[:idx_child_post+1]
            post_right = post[idx_child_post+1:-1]

            if not pre_left:
                node.left = construct(pre_right, post_left)
            else:
                node.left  = construct(pre_left, post_left)
                node.right = construct(pre_right, post_right)

            return node

        return construct(pre, post)

