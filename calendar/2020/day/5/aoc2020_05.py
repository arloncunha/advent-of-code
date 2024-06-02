# --- Day 5: Binary Boarding ---
# https://adventofcode.com/2020/day/5


def column(code):
    min = 0
    max = 7
    # print(min, max)
    for i in range(3):
        if code[i + 7] == 'L':
            max = int((max + min) / 2)
        else:
            min = int((max + min) / 2)
        # print(min, max)
    return max


def row(code):
    min = 0
    max = 127
    # print(code)
    # print(min, max)
    for i in range(7):
        if code[i] == 'F':
            max = int((max + min) / 2)
        else:
            min = int((max + min) / 2)
        # print(min, max)
    return max


seats = []
with open('input.txt', 'r') as reader:
    input = [i.strip() for i in reader.readlines()]
for line in input:
    # print(line)
    # print(row(line))
    # print(column(line))
    seats.append(row(line)*8+column(line))
seats.sort()
seats.reverse()
print(seats[0])

aux = seats[0]+1
for seat in seats:
    if aux - seat != 1:
        print(seat+1)
    aux = seat
