# AoC 2024 Day 4
# todo: use logging or do something else so we
# \can tune the outputs for exceptions
# or avoid them altogether.

class Parser():
    def __init__(self):
        with open('input.txt', 'r') as f:
            input = f.readlines()
        self.input = input
        self.sum = 0
        self.xmas_crosses = 0

    def check_horizontal(self):
        for line in self.input:
            # If equal to X starter...
            # add 3 and see if those are MAS
            for idx, char in enumerate(line):
                if char == 'X':
                    if line[idx:idx+4] == "XMAS":
                        self.sum += 1
                # todo: should check we aren't out of index
                # just relying on luck rn.
                if char == 'S':
                    if line[idx:idx+4] == "SAMX":
                        # print("Found backwards XMAS")
                        self.sum += 1

    def check_vertical(self):
        for y_idx, line in enumerate(self.input):
            for x_idx, char in enumerate(line):
                try:
                    candidate = (
                                    char +
                                    self.input[y_idx+1][x_idx] +
                                    self.input[y_idx+2][x_idx] +
                                    self.input[y_idx+3][x_idx]
                    )
                except Exception as e:
                    # print(f"exception {e}")
                    pass
                if candidate == "XMAS":
                    self.sum += 1
                elif candidate == "SAMX":
                    self.sum += 1

    def check_diagonal_left_slant(self):
        for y_idx, line in enumerate(self.input):
            for x_idx, char in enumerate(line):
                try:
                    candidate = (
                                    char +
                                    self.input[y_idx+1][x_idx+1] +
                                    self.input[y_idx+2][x_idx+2] +
                                    self.input[y_idx+3][x_idx+3]
                    )
                except Exception as e:
                    # print(f"exception {e}")
                    pass
                if candidate == "XMAS":
                    self.sum += 1
                elif candidate == "SAMX":
                    self.sum += 1

    def check_diagonal_right_slant(self):
        for y_idx, line in enumerate(self.input):
            for x_idx, char in enumerate(line):
                try:
                    candidate = (
                                    char +
                                    self.input[y_idx+1][x_idx-1] +
                                    self.input[y_idx+2][x_idx-2] +
                                    self.input[y_idx+3][x_idx-3]
                    )
                except Exception as e:
                    # print(f"exception {e}")
                    pass
                if candidate == "XMAS":
                    self.sum += 1
                elif candidate == "SAMX":
                    self.sum += 1

    def find_cross_xmas(self):
        # if we find an A...then check if there is a MAS
        # check if the x-1, y-1 + self + x+1, y+1 == SAM or MAS and SAM or MAS
        for y_idx, line in enumerate(self.input):
            for x_idx, char in enumerate(line):
                if x_idx >= 1 and x_idx <= 139 and y_idx >= 1 and y_idx <= 139:
                    if char == "A":
                        try:
                            left_slant = (
                                            self.input[y_idx-1][x_idx-1] +
                                            char +
                                            self.input[y_idx+1][x_idx+1]
                            )
                            right_slant = (
                                            self.input[y_idx-1][x_idx+1] +
                                            char +
                                            self.input[y_idx+1][x_idx-1]
                            )
                        except Exception as e:
                            # print(f"exception {e}")
                            pass
                        if (
                            (left_slant == "MAS" or left_slant == "SAM") and
                            (right_slant == "MAS" or right_slant == "SAM")
                        ):
                            self.xmas_crosses += 1

        print(f"Day 4 Part 2 answer is {self.xmas_crosses}")


if __name__ == '__main__':
    parser = Parser()
    parser.check_horizontal()
    parser.check_vertical()
    parser.check_diagonal_left_slant()
    parser.check_diagonal_right_slant()
    print(f"Day 4 Part 1 answer {parser.sum}")
    parser.find_cross_xmas()
