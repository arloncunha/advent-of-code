# --- Day 9: Encoding Error ---
# https://adventofcode.com/2020/day/9

def is_valid(n, preamble_list):
    result = False
    for i in preamble_list:
        for j in preamble_list:
            if i == j:
                continue
            if n == i + j:
                result = True
                break
    return result


with open('input.txt', 'r') as reader:
    input = [int(i.strip()) for i in reader.readlines()]

preamble_size = 25
part1 = 0
for i in range(preamble_size, len(input)):
    valid = is_valid(input[i], input[i - preamble_size: i])
    if not valid:
        part1 = input[i]
        break
print(part1)

part2 = 0
for i in range(input.index(part1)):
    for j in range(i+1, input.index(part1)):
        part2 = sum(input[i:j])
        if part2 == part1:
            print(sorted(input[i:j])[0]+sorted(input[i:j])[len(input[i:j])-1])
            break
