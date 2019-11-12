import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = len(arr)
        idx = bisect.bisect_left(arr, x)
        i, j = idx-1, idx
        elements = []
        for _ in range(k):
            if i < 0:
                elements.append(arr[j])
                j += 1
            elif j >= l:
                elements = [arr[i]] + elements
                i -= 1
            else:
                if x-arr[i] <= arr[j]-x:
                    elements = [arr[i]] + elements
                    i -= 1
                else:
                    elements.append(arr[j])
                    j += 1
        return elements
