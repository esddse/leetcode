class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: 
            if not s:
                return True 
            else:
                return False
        else:
            if not s:
                if len(p) > 1:
                    if p[1] != "*":
                        return False
                    return self.isMatch(s, p[2:])
                else:
                    return False
            else:
                if len(p) > 1:
                    if p[1] == "*":
                        if p[0] == "." or p[0] == s[0]: 
                            return self.isMatch(s[1:], p[:]) or self.isMatch(s[:], p[2:])
                        else: 
                            return self.isMatch(s[:], p[2:])
                    else:
                        if p[0] == "." or p[0] == s[0]:
                            return self.isMatch(s[1:], p[1:])
                        else:
                            return False
                else: # len(p) == 1
                    if p[0] == "." or p[0] == s[0]:
                        return self.isMatch(s[1:], p[1:])
                    else:
                        return False
                
                    
            
        
        