class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(num) for num in version1.split(".")]
        version2 = [int(num) for num in version2.split(".")]
        size1, size2 = len(version1), len(version2)
        if size1 < size2:
            version1 += [0] * (size2 - size1)
        else:
            version2 += [0] * (size1 - size2)
        size = max(size1, size2)
        for i in range(size):
            if version1[i] > version2[i]:
                return 1 
            elif version2[i] > version1[i]:
                return -1
        return 0
        