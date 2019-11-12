class Solution:
    def solveEquation(self, equation: str) -> str:
        left_exp, right_exp = equation.split("=")

        def parse(exp):
            result = {"x":0, "const": 0}
            i = 0
            is_plus = 1
            coefficient = 0
            while i < len(exp):
                if exp[i] == "+":
                    result["const"] += coefficient * is_plus
                    is_plus = 1
                    coefficient = 0
                elif exp[i] == "-":
                    result["const"] += coefficient * is_plus
                    is_plus = -1
                    coefficient = 0
                elif exp[i] == "x":
                    if i == 0 or exp[i-1] == "+" or exp[i-1] == "-":
                        result["x"] += is_plus
                    else:
                        result["x"] += coefficient * is_plus
                    coefficient = 0
                else:
                    coefficient = coefficient * 10 + int(exp[i])
                i += 1
            if coefficient:
                result["const"] += coefficient * is_plus
            return result

        left_result  = parse(left_exp)
        right_result = parse(right_exp)

        if left_result["x"] == right_result["x"]:
            if left_result["const"] == right_result["const"]:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x = (right_result["const"]-left_result["const"]) // (left_result["x"]-right_result["x"]) 
            return "x="+str(x)




