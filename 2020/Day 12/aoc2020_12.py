# --- Day 12: Rain Risk ---
# https://adventofcode.com/2020/day/12


# remarks:
# credits to https://dev.to/saripius/comment/195el for part2
#  - failing direction E W  and rotate 180 (keep vars * -1)

def distance1(action_input):
    compass = ['E', 'N', 'W', 'S']
    facing = 'E'
    x = 0
    y = 0
    for line in action_input:
        # print("".join(line))
        # print("                                            ", end="")
        if line[0] == 'F':
            line[0] = facing
        elif line[0] == 'L':
            ci = compass.index(facing)        # current index
            dr = int("".join(line[1:])) / 90  # degress to rotate
            idx = int((ci + dr) % 4)
            facing = compass[idx]
        elif line[0] == 'R':
            ci = compass[::-1].index(facing)  # current index
            dr = int("".join(line[1:])) / 90  # degress to rotate
            idx = int((ci + dr) % 4)
            facing = compass[::-1][idx]
        if line[0] == 'N':
            y = y + int("".join(line[1:]))
        elif line[0] == 'S':
            y = y - int("".join(line[1:]))
        if   line[0] == 'E':
            x = x - int("".join(line[1:]))
        elif line[0] == 'W':
            x = x + int("".join(line[1:]))
    return abs(x) + abs(y)

def distance2(action_input):
    x = 0
    y = 0
    way_x = 10
    way_y = 1
    for line in action_input:
        if line[0] == 'F':
            x = x + way_x * int("".join(line[1:]))
            y = y + way_y * int("".join(line[1:]))
        elif "".join(line) == 'R90':
            way_x, way_y = way_y * 1, way_x * -1
        elif "".join(line) == 'R180':
            way_x, way_y = way_x * -1, way_y * -1
        elif "".join(line) == 'R270':
            way_x, way_y = way_y * -1, way_x * 1
        elif "".join(line) == 'L90':
            way_x, way_y = way_y * -1, way_x * 1
        elif "".join(line) == 'L180':
            way_x, way_y = way_x * -1, way_y * -1
        elif "".join(line) == 'L270':
            way_x, way_y = way_y * 1, way_x * -1
        elif line[0] == 'N':
            way_y = way_y + int("".join(line[1:]))
        elif line[0] == 'S':
            way_y = way_y - int("".join(line[1:]))
        if   line[0] == 'E':
            way_x = way_x + int("".join(line[1:]))
        elif line[0] == 'W':
            way_x = way_x - int("".join(line[1:]))
        # input()
        # print("x: ", x, " | ", end="")
        # print("y: ", y, " | ", end="")
        # print("wx: ", way_x, " | ", end="")
        # print("wy: ", way_y, " | ", end="")
        # print("".join(line), " | ", end="")
        # input()
    # print("x: ", x, " | ", end="")
    # print("y: ", y, " | ", end="")
    return abs(x) + abs(y)


with open('input.txt', 'r') as reader:
    input_file = [list(i.strip()) for i in reader.readlines()]

print(distance1(input_file))

with open('input.txt', 'r') as reader:
    input_file = [list(i.strip()) for i in reader.readlines()]

print(distance2(input_file))

# x:  -95  | y:  -73909  | 74004
#x:  32283  | y:  -24145  | 56428
