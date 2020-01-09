class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {}
        self.head = Node("#", "#")
        self.tail = Node("#", "#")
        self.head.next = self.tail 
        self.tail.prev = self.head
        
    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev
        
    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.remove(node)
            self.add(node)
            return
        if len(self.key2node) == self.capacity:
            del self.key2node[self.head.next.key]
            self.remove(self.head.next)
        node = Node(key, value)
        self.key2node[key] = node 
        self.add(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)