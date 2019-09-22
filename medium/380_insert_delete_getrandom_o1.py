
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items   = []
        self.val2idx = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.val2idx.get(val) is None:
            self.val2idx[val] = len(self.items)
            self.items.append(val)
            return True 
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if self.val2idx.get(val) is None:
            return False
        else:
            idx, last = self.val2idx[val], self.items[-1]
            self.items[idx] = last
            self.items.pop()
            self.val2idx[last] = idx
            self.val2idx[val] = None
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.items)-1)
        return self.items[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()