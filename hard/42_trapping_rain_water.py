class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0] + height + [0]
        size = len(height)
        peaks = []
        for i in range(1, size-1):
            if height[i-1] < height[i] >= height[i+1]:
                peaks.append((height[i], i))
        peaks = sorted(peaks, key=lambda item: item[0], reverse=True)
        area = 0
        xr, xl = None, None
        for h, i in peaks:
            if not xr:
                xr, xl = i, i 
            else:
                if xl < i < xr:
                    continue
                elif i < xl:
                    l, r = i, xl
                    xl = i
                else:
                    l, r = xr, i 
                    xr = i
                for j in range(l+1, r):
                    area += max(height[i]-height[j], 0)
        return area