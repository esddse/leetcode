import math
import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = math.sqrt(random.random()) * self.radius
        theta = random.random() * math.pi * 2
        x = r * math.cos(theta) + self.x_center
        y = r * math.sin(theta) + self.y_center
        return [x, y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()