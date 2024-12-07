left_nums = []
right_nums = []

with open('input.txt', 'r') as file:
  for line in file:
    fmtd_line = line.rstrip('\n').split('   ')
    left_nums.append(fmtd_line[0])
    right_nums.append(fmtd_line[1])


left_nums.sort()
right_nums.sort()


sim_scores = []

# for each number in LEFT LIST
for num in left_nums:
  # find how many times it occurs in the right list
  # save the frequency as a similarity score and multiply the left number by it.
  frequency = right_nums.count(num)

  sim_score = frequency * int(num)

  sim_scores.append(int(sim_score))

print(f"The answer to AoC 2024, Part 2 is: {sum(sim_scores)}")