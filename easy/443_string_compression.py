class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        if not chars:
            return 0

        last = chars[0]
        cnt = 1
        i = 0
        for j in range(1, len(chars)):
            if chars[j] != last:
                if cnt == 1:
                    chars[i] = last
                    i += 1
                else:
                    chars[i] = last
                    i += 1
                    cnt = list(str(cnt))
                    for k in range(len(cnt)):
                        chars[i] = cnt[k]
                        i += 1
                last = chars[j]
                cnt = 1
            else:
                cnt += 1
        if cnt == 1:
            chars[i] = last
            i += 1
        else:
            chars[i] = last
            i += 1
            cnt = list(str(cnt))
            for k in range(len(cnt)):
                chars[i] = cnt[k]
                i += 1
        return i