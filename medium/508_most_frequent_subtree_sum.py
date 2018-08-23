# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter

        if not root:
            return []

        def subtreeSum(root):
            if not root.left and not root.right:
                return root.val, Counter([root.val])
            root_sum = root.val
            root_counter = Counter()
            if root.left:
                left_sum, left_counter = subtreeSum(root.left)
                root_sum += left_sum
                root_counter.update(left_counter)
            if root.right:
                right_sum, right_counter = subtreeSum(root.right)
                root_sum += right_sum
                root_counter.update(right_counter)
            root_counter.update([root_sum])
            return root_sum, root_counter

        __, root_counter = subtreeSum(root)
        root_counter = root_counter.most_common()
        sum_lst = [root_counter[0][0]]
        max_cnt = root_counter[0][1]
        for num, cnt in root_counter[1:]:
            if cnt < max_cnt:
                break
            else:
                sum_lst.append(num)
        return sum_lst


        