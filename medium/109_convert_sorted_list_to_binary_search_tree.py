# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        if prev:
            prev.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node