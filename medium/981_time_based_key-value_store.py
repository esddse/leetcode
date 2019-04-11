
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.mem = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key not in self.mem:
            self.mem[key] = [(timestamp, value)]
        else:
            self.mem[key] = [(timestamp, value)] + self.mem[key]

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if self.mem[key]:
            for t, v in self.mem[key]:
                if t <= timestamp:
                    return v 
            return ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)