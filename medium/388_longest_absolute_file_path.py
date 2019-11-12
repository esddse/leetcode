class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        files = input.split("\n")

        def parse_file(file):
            cnt = 0
            while file[cnt] == "\t":
                cnt += 1
            file = file[cnt:]
            return cnt, file

        abs_path = []
        max_length = 0
        for file in files:
            depth, file = parse_file(file)
            if not abs_path:
                abs_path.append((depth, len(file)))
            else:
                while abs_path and abs_path[-1][0] >= depth:
                    abs_path.pop()
                abs_path.append((depth, len(file)))
            if "." in file:
                length = sum([item[1] for item in abs_path]) + len(abs_path) - 1
                max_length = max(max_length, length)
        return max_length

