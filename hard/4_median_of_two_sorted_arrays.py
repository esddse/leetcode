class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1, size2 = len(nums1), len(nums2)
        if size1 > size2:
            nums1, nums2 = nums2, nums1
            size1, size2 = size2, size1
        
        l, r, half_size = 0, size1, (size1 + size2 + 1) // 2
        while l <= r:
            m = (l + r) // 2
            n = half_size - m
            if 0<=m<size1 and nums2[n-1] > nums1[m]:
                l = m + 1
            elif 0<m<=size1 and nums1[m-1] > nums2[n]:
                r = m
            else:
                left1  = nums1[m-1] if 0<=m-1<size1 else None
                left2  = nums2[n-1] if 0<=n-1<size2 else None
                right1 = nums1[m] if 0<=m<size1 else None
                right2 = nums2[n] if 0<=n<size2 else None
                
                if not left1:
                    max_left = left2
                elif not left2:
                    max_left = left1
                else:
                    max_left = max(left1, left2)
                    
                if not right1:
                    min_right = right2
                elif not right2:
                    min_right = right1
                else:
                    min_right = min(right1, right2)
                
                
                if (size1 + size2) % 2 == 1:
                    return max_left 
                else:
                    return (max_left + min_right) / 2