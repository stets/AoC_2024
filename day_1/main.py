# Advent of Code 2024, Day 1, Parts 1 and 2

def read_nums():
    left_nums = []
    right_nums = []

    with open('input.txt', 'r') as file:
        for line in file:
            fmtd_line = line.rstrip('\n').split('   ')
            left_nums.append(fmtd_line[0])
            right_nums.append(fmtd_line[1])

    left_nums.sort()
    right_nums.sort()
    return left_nums, right_nums


def part_one(left_nums, right_nums):
    distances = []
    for idx, num in enumerate(left_nums):
        distance = int(left_nums[idx]) - int(right_nums[idx])
        distance = abs(distance)
        distances.append(distance)
    print(f"The answer to AoC 2024 Day 1 , Part 1 is: {sum(distances)}")


def part_two(left_nums, right_nums):
    sim_scores = []
    for num in left_nums:
        frequency = right_nums.count(num)
        sim_score = frequency * int(num)
        sim_scores.append(int(sim_score))

    print(f"The answer to AoC 2024, Part 2 is: {sum(sim_scores)}")


if __name__ == '__main__':
    left_nums, right_nums = read_nums()
    part_one(left_nums, right_nums)
    part_two(left_nums, right_nums)
