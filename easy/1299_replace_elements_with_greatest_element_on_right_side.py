class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        max_num = -1
        for i in range(size-1, -1, -1):
            if arr[i] > max_num:
                max_num, arr[i] = arr[i], max_num
            else:
                arr[i] = max_num
        return arr
