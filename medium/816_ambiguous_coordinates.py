class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        
        def is_valid_int(num):
            if not num:
                return False
            if num[0] == "0":
                if len(num) == 1:
                    return True 
                else:
                    return False
            else:
                return True

        def is_valid_float(num):
            before, after = num.split(".")
            if not before or not after:
                return False
            if before[0] == "0":
                if len(before) > 1:
                    return False 
            if after[-1] == "0":
                return False
            return True

        S = S[1:-1]
        res = []
        for i in range(len(S)):
            num1, num2 = S[:i], S[i:]
            if is_valid_int(num1) and is_valid_int(num2):
                res.append((num1, num2))

            for j in range(len(num1)):
                float1 = num1[:j] + "." + num1[j:]
                if is_valid_float(float1) and is_valid_int(num2):
                    res.append((float1, num2))

            for j in range(len(num2)):
                float2 = num2[:j] + "." + num2[j:]
                if is_valid_int(num1) and is_valid_float(float2):
                    res.append((num1, float2))

            for j in range(len(num1)):
                float1 = num1[:j] + "." + num1[j:]
                if not is_valid_float(float1):
                    continue
                for k in range(len(num2)):
                    float2 = num2[:k] + "." + num2[k:]
                    if is_valid_float(float2):
                        res.append((float1, float2))

            
        res = ["("+num1+", "+num2+")" for num1, num2 in res]
        return res


