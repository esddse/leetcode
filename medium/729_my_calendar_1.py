class Node:
    def __init__(self, s, e):
        self.s = s 
        self.e = e 
        self.left  = None 
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True

        def check(s, e, node):
            if e <= node.s:
                if not node.left:
                    node.left = Node(s, e)
                    return True 
                else:
                    return check(s, e, node.left)
            elif s >= node.e:
                if not node.right:
                    node.right = Node(s, e)
                    return True 
                else:
                    return check(s, e, node.right)
            else:
                return False
        return check(start, end, self.root)


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)