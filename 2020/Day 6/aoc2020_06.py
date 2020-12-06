# --- Day 6: Custom Customs ---
# https://adventofcode.com/2020/day/6

group = ''
part1 = 0
with open('input.txt', 'r') as reader:
    input = [i.strip() for i in reader.readlines()]
for line in input:
    if len(line) == 0:
        part1 = part1 + len(''.join(set(group)))
        group = ''
        continue
    group = group + line
if group != '':
    part1 = part1 + len(''.join(set(group)))
print(part1)

group = ''
people = 0
part2 = 0
for line in input:
    if len(line) == 0:
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if group.count(letter) == people:
                part2 = part2 + 1
        group = ''
        people = 0
        continue
    group = group + ''.join(set(line))
    people = people + 1
if group != '':
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if group.count(letter) == people:
            part2 = part2 + 1
print(part2)
