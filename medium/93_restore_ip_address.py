class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        ans = []
        
        def dfs(ip, s, step, ans):
            if step == 4:
                if len(s) == 1 or (len(s) > 1 and s[0] != "0" and int(s) <= 255):
                    ans.append(ip+"."+s)
            else:
                if not s:
                    return 
                if len(s) >= 1:
                    nip = ip+"."+s[:1] if ip else s[:1]
                    dfs(nip, s[1:], step+1, ans)
                if len(s) >= 2 and s[0] != "0":
                    nip = ip+"."+s[:2] if ip else s[:2]
                    dfs(nip, s[2:], step+1, ans)
                if len(s) >= 3 and s[0] != "0" and int(s[:3]) <= 255:
                    nip = ip+"."+s[:3] if ip else s[:3]
                    dfs(nip, s[3:], step+1, ans)
                    
        dfs("", s, 1, ans)
        return ans