class Parser():
    def __init__(self):
        with open('input.txt', 'r') as f:
            input = f.readlines()
        self.input = input
        self.sum = 0

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
                                    self.input[y_idx][x_idx] +
                                    self.input[y_idx+1][x_idx] +
                                    self.input[y_idx+2][x_idx] +
                                    self.input[y_idx+3][x_idx]
                    )
                    print(candidate)
                except Exception as e:
                    print(f"exception {e}")
                if candidate == "XMAS":
                    self.sum += 1
                elif candidate == "SAMX":
                    self.sum += 1

    def check_diagonal_left_slant(self):
        for y_idx, line in enumerate(self.input):
            for x_idx, char in enumerate(line):
                try:
                    candidate = (
                                    self.input[y_idx][x_idx] +
                                    self.input[y_idx+1][x_idx+1] +
                                    self.input[y_idx+2][x_idx+2] +
                                    self.input[y_idx+3][x_idx+3]
                    )
                    print(candidate)
                except Exception as e:
                    print(f"exception {e}")
                if candidate == "XMAS":
                    self.sum += 1
                elif candidate == "SAMX":
                    self.sum += 1

    def check_diagonal_right_slant(self):
        for y_idx, line in enumerate(self.input):
            for x_idx, char in enumerate(line):
                try:
                    candidate = (
                                    self.input[y_idx][x_idx] +
                                    self.input[y_idx+1][x_idx-1] +
                                    self.input[y_idx+2][x_idx-2] +
                                    self.input[y_idx+3][x_idx-3]
                    )
                    print(candidate)
                except Exception as e:
                    print(f"exception {e}")
                if candidate == "XMAS":
                    self.sum += 1
                elif candidate == "SAMX":
                    self.sum += 1


if __name__ == '__main__':
    parser = Parser()
    parser.check_horizontal()
    parser.check_vertical()
    parser.check_diagonal_left_slant()
    parser.check_diagonal_right_slant()
    print(f"Day 4 Part 1 answer {parser.sum}")
