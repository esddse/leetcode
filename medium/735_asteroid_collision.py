class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                if asteroid < 0:
                    while asteroid and stack and stack[-1] > 0:
                        if stack[-1] > -asteroid:
                            asteroid = None
                        elif stack[-1] == -asteroid:
                            stack.pop()
                            asteroid = None
                        else:
                            stack.pop()
                    if asteroid:
                        stack.append(asteroid)
                else:
                    stack.append(asteroid)
        return stack