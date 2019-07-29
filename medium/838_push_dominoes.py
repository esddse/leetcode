class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        size = len(dominoes)
        if size <= 1:
            return dominoes
        dominoes = list(dominoes)
        
        cnt = 1
        while cnt:
            cnt = 0
            new_dominoes = []
            for i in range(size):
                if dominoes[i] == ".":
                    if i == 0:
                        if dominoes[i+1] == "L":
                            new_dominoes.append("L")
                            cnt += 1
                        else:
                            new_dominoes.append(dominoes[i])
                    elif i == size - 1:
                        if dominoes[i-1] == "R":
                            new_dominoes.append("R")
                            cnt += 1
                        else:
                            new_dominoes.append(dominoes[i])
                    else:
                        if dominoes[i+1] == "L" and dominoes[i-1] == "R":
                            new_dominoes.append(dominoes[i])
                        elif dominoes[i+1] == "L":
                            new_dominoes.append("L")
                            cnt += 1
                        elif dominoes[i-1] == "R":
                            new_dominoes.append("R")
                            cnt += 1
                        else:
                            new_dominoes.append(dominoes[i])
                else:
                    new_dominoes.append(dominoes[i])
            dominoes = new_dominoes
        return "".join(dominoes)

