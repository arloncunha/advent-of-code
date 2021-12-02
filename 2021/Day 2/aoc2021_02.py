# --- Day 2: Dive! ---
# https://adventofcode.com/2021/day/2
import re

x = 0
y = 0
x2 = 0
y2 = 0
aim = 0
with open("input.txt", 'r') as reader:
    input = [i.strip() for i in reader.readlines()]
for line in input:
    m = re.search(r"(\D+) (\d+)", line)
    if m.group(1) == 'forward':
        x = x + int(m.group(2))
        x2 = x2 + int(m.group(2))
        y2 = y2 + aim * int(m.group(2))
    elif m.group(1) == 'down':
        y = y + int(m.group(2))
        aim = aim + int(m.group(2))
    elif m.group(1) == 'up':
        y = y - int(m.group(2))
        aim = aim - int(m.group(2))
print x * y
print x2 * y2
