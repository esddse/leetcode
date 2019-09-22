class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        stack = []
        max_len = 0
        cnt = [0, 0]
        for apple in tree:
            if len(stack) == 0:
                stack.append(apple)
                cnt[0] = 1
            elif len(stack) == 1:
                if apple == stack[0]:
                    cnt[0] += 1
                else:
                    stack.append(apple)
                    cnt[0] += 1
                    cnt[1] = 1
            else:
                if apple == stack[0]:
                    stack[0], stack[1] = stack[1], stack[0]
                    cnt[0] += 1
                    cnt[1] = 1
                elif apple == stack[1]:
                    cnt[0] += 1
                    cnt[1] += 1
                else:
                    max_len = max(max_len, cnt[0])
                    stack[0] = stack[1]
                    stack[1] = apple
                    cnt[0] = cnt[1] + 1
                    cnt[1] = 1
        max_len = max([max_len]+cnt)
        return max_len
