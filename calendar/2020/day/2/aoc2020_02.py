# --- Day 2: Password Philosophy ---
# https://adventofcode.com/2020/day/2
import re


def is_valid_password_part1(min, max, letter, password):
    if password.count(letter) >= min and password.count(letter) <= max:
        return 1
    else:
        return 0


def is_valid_password_part2(min, max, letter, password):
    password = "0" + password
    if min > len(password):
        min = 0

    if max > len(password):
        max = 0
    if (password[min] == letter and password[max] != letter) or \
       (password[min] != letter and password[max] == letter):
        return 1
    else:
        return 0


part1 = 0
part2 = 0
with open("input.txt", 'r') as reader:
    input = [i.strip() for i in reader.readlines()]
for line in input:
    m = re.search(r"(\d+)-(\d+) (.): (.+)", line)
    part1 = part1 + is_valid_password_part1(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))  # noqa : E501
    part2 = part2 + is_valid_password_part2(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))  # noqa : E501

print(part1)
print(part2)
