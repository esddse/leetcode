class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.order = []
        

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlap:
            if not (start >= j or end <= i):
                return False
        for i, j in self.order:
            if not (start >= j or end <= i):
                self.overlap.append((max(start, i), min(end, j)))
        self.order.append((start, end))
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)



