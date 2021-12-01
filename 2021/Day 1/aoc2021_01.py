# --- Day 1: Sonar Sweep ---
# https://adventofcode.com/2021/day/1

result = 0
with open('input.txt', 'r') as reader:
    input = [int(i.strip()) for i in reader.readlines()]

part1 = 0
part2 = 0
for i in range(len(input) - 1):
    part1 = part1 + int(input[i+1] > input[i])
for i in range(len(input) - 3):
    part2 = part2 + int((input[i+3] + input[i+2] + input[i+1]) > (input[i+2] + input[i+1] + input[i]))

print part1
print part2
