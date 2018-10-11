from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        res = []
        for k, cnt1 in counter1.items():
            cnt2 = counter2[k]
            if cnt2:
                res += [k] * min(cnt1, cnt2)
        return res