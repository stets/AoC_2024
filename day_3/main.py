import re


class Parser():
    def __init__(self):
        with open('input.txt', 'r') as f:
            input = f.read()

        self.input = input
        self.total = 0

    # parse the corrupt memory
    def parse_mults(self, pattern):
        matches = re.findall(pattern, self.input)
        return matches

    def mult(self, input, ignore_booleans=True):
        enabled = True
        self.total = 0
        for each in input:
            if enabled and 'mul(' in each:
                x, y = each.strip('mul(').strip(')').split(',')
                self.total += int(x) * int(y)
            elif "don't()" in each:
                enabled = False if not ignore_booleans else True
            elif "do()" in each:
                enabled = True if not ignore_booleans else True
        return self.total


if __name__ == '__main__':
    parser = Parser()
    mul_match = r'don\'t\(\)|do\(\)|mul\(\d+,\d+\)'
    matches = parser.parse_mults(mul_match)

    part_one = parser.mult(matches)
    part_two = parser.mult(matches, ignore_booleans=False)
    print(f"Day 3 Part 1 answer is {part_one}")
    print(f"Day 3 Part 2 answer is {part_two}")
