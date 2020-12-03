# --- Day 3: Toboggan Trajectory ---
# https://adventofcode.com/2020/day/3
import re


part1 = 0
with open("input.txt", 'r') as reader:
    input = [i.strip() for i in reader.readlines()]

for i, line in enumerate(input):
    if i == 0:
        continue
    if line[(i * 3) % len(line)] == "#":
        part1 = part1 + 1

print(part1)

slop1 = 0
slop2 = 0
slop3 = 0
slop4 = 0
slop5 = 0
for i, line in enumerate(input):
    if i == 0:
        continue
    if line[(i * 1) % len(line)] == "#":
        slop1 = slop1 + 1
    if line[(i * 3) % len(line)] == "#":
        slop2 = slop2 + 1
    if line[(i * 5) % len(line)] == "#":
        slop3 = slop3 + 1
    if line[(i * 7) % len(line)] == "#":
        slop4 = slop4 + 1
    if (i + 2) % 2 == 0 and line[int(i / 2) % len(line)] == "#":
        slop5 = slop5 + 1

print(slop1 * slop2 * slop3 * slop4 * slop5)
