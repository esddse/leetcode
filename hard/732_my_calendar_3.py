
class Node:
    def __init__(self, start, end):
        self.val = 0
        self.to_add_left  = 0
        self.to_add_right = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None 

class MyCalendarThree:

    def __init__(self):
        self.tree = Node(0, 1e9)

    def add(self, node, to_add, start, end):
        node.val += to_add

        node_val   = node.val
        node_start = node.start
        node_end   = node.end
        node_mid   = (node_start + node_end) // 2

        if not node_start == node_end:
            node.to_add_left  += to_add
            node.to_add_right += to_add

        if start == node_start and end == node_end:
            node.val += 1
            if not node_start == node_end:
                node.to_add_left  += 1
                node.to_add_right += 1
            return node.val

        if node_mid < start:
            if not node.right:
                node.right = Node(node_mid+1, node_end)
            node.val = max(self.add(node.right, node.to_add_right, start, end), node_val)
            node.to_add_right = 0
        elif node_mid >= end:
            if not node.left:
                node.left = Node(node_start, node_mid)
            node.val = max(self.add(node.left, node.to_add_left, start, end), node_val)
            node.to_add_left = 0
        else:
            if not node.right:
                node.right = Node(node_mid+1, node_end)
            if not node.left:
                node.left = Node(node_start, node_mid)
            max_left  = self.add(node.left, node.to_add_left, start, node_mid)
            max_right = self.add(node.right, node.to_add_right, node_mid+1, end)
            node.to_add_left = 0
            node.to_add_right = 0
            node.val  = max([max_left, max_right, node_val])
        return node.val
    


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """

        self.add(self.tree, 0, start, end-1)
        return self.tree.val


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
