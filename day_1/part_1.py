left_nums = []
right_nums = []

with open('input.txt', 'r') as file:
  for line in file:
    fmtd_line = line.rstrip('\n').split('   ')
    left_nums.append(fmtd_line[0])
    right_nums.append(fmtd_line[1])


left_nums.sort()
right_nums.sort()

distances = []

for idx, num in enumerate(left_nums):
  distance = int(left_nums[idx]) - int(right_nums[idx])
  distance = abs(distance)
  distances.append(distance)

answer = sum(distances)
print(f"The answer to AoC 2024 Day 1 , Part 1 is: {answer}")
