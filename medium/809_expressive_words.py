class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def transform(s):
            lst = []
            pre_c = None 
            cnt = 0
            for c in s:
                if not pre_c:
                    pre_c = c 
                    cnt = 1
                else:
                    if c != pre_c:
                        lst.append((pre_c, cnt))
                        pre_c = c 
                        cnt = 1
                    else:
                        cnt += 1
            lst.append((pre_c, cnt))
            return lst

        lstS = transform(S)
        cnt = 0
        for word in words:
            lstword = transform(word)
            if len(lstS) != len(lstword):
                continue
            valid = True
            for item1, item2 in zip(lstS, lstword):
                cS, cntS = item1
                cword, cntword = item2
                if cS != cword or cntword > cntS:
                    valid = False
                    break
                if cntword < cntS and cntS < 3:
                    valid = False 
                    break
            if valid:
                cnt += 1
        return cnt


