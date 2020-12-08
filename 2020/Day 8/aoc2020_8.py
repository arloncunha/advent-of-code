# --- Day 8: Handheld Halting ---
# https://adventofcode.com/2020/day/8
import re


def run_program(code, replace_pos):
    i = 0
    j = 0
    accumulator = 0
    while code[i] != '':
        instruction = code[i].group(1)
        if replace_pos != -1 and i == replace_pos:
            if instruction == 'nop':
                instruction = 'jmp'
            elif instruction == 'jmp':
                instruction = 'nop'
        j = i
        if instruction == 'acc':
            accumulator = accumulator + int(code[i].group(2))
            i = i + 1
        elif instruction == 'jmp':
            i = i + int(code[i].group(2))
        elif instruction == 'nop':
            i = i + 1
        code[j] = ''
    if replace_pos != -1 and i < len(code) - 1:
        accumulator = ''
    return accumulator


with open('input.txt', 'r') as reader:
    input = [i.strip() for i in reader.readlines()]

code = []
for line in input:
    m = re.match(r"(\S+) (.\d+)", line)
    code.append(m)

code.append('')  # append halt condition
print(run_program(code.copy(), -1))

part2 = ''
for i in range(len(code)):
    part2 = run_program(code.copy(), i)
    if part2 != '':
        print(part2)
        break
