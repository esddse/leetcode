class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return sum([val for key, val in self.map.items() if key.startswith(prefix)])