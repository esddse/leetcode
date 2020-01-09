class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return None
        global max_sum
        max_sum = -float("inf")
        def dfs(node):
            sum_left, sum_right = -float("inf"), -float("inf")
            if node.left:
                sum_left = dfs(node.left)
            if node.right:
                sum_right = dfs(node.right)
            max_node_sum = max([node.val, node.val+sum_left, node.val+sum_right, node.val+sum_left+sum_right])
            global max_sum
            max_sum = max(max_sum, max_node_sum)
            return max(node.val+sum_left, node.val+sum_right, node.val)
        dfs(root)
        return max_sum