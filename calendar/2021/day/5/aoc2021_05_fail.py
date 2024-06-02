#!/usr/bin/env python3
# --- Day 5: Hydrothermal Venture ---
# https://adventofcode.com/2021/day/5

import re

# ------------- DEBUG SESSION --------------

class BackgroundColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_red(skk, end=""): print("\033[91m {}\033[00m" .format(skk), end=end)           # noqa:E704
def print_green(skk, end=""): print("\033[92m {}\033[00m" .format(skk), end=end)         # noqa:E704
def print_yellow(skk, end=""): print("\033[93m {}\033[00m" .format(skk), end=end)        # noqa:E704
def print_light_purple(skk, end=""): print("\033[94m {}\033[00m" .format(skk), end=end)  # noqa:E704
def print_purple(skk, end=""): print("\033[95m {}\033[00m" .format(skk), end=end)        # noqa:E704
def print_cyan(skk, end=""): print("\033[96m {}\033[00m" .format(skk), end=end)          # noqa:E704
def print_light_gray(skk, end=""): print("\033[97m {}\033[00m" .format(skk), end=end)    # noqa:E704
def print_black(skk, end=""): print("\033[98m {}\033[00m" .format(skk), end=end)         # noqa:E704

def debug_print(skk, end="\n"):
    if not __debug__:
        return
    print_red(skk, end)

def debug_log(skk):
    if not __debug__:
        return
    print(skk)

# ------------- DATA --------------

class PuzzleData:
    """Data Section, declares global vars used accross the puzzle
       UPPERCASE_VARIABLE: to be used as constants (not locked!)
    """
    lines:   list = []  # noqa


# ------------- DECLARATIONS --------------

def intersect_points_new(a, b, c, d):
    """ there are only 3 types of lines:
        - vertical is when x1 equal x2
        - horizontal is when y1 equal y2
        - diagonal (45%) is when abs(x1 - x2) = abs(y1 - y2)
    """

    l1_x_distance = a[0] - b[0]
    l1_y_distance = a[1] - b[1]

    if l1_x_distance == 0:
        l1_steps = abs(l1_y_distance) + 1
        l1_step_x = 0
        l1_step_y = 1 if b[1] > a[1] else -1
    elif l1_y_distance == 0:
        l1_steps = abs(l1_x_distance) + 1
        l1_step_y = 0
        l1_step_x = 1 if b[0] > a[0] else -1
    else:
        l1_steps = abs(l1_x_distance) + 1
        l1_step_x = 1 if b[0] > a[0] else -1
        l1_step_y = 1 if b[1] > a[1] else -1

    l2_x_distance = c[0] - d[0]
    l2_y_distance = c[1] - d[1]

    if l2_x_distance == 0:
        l2_steps = abs(l2_y_distance) + 1
        l2_step_x = 0
        l2_step_y = 1 if d[1] > d[1] else -1
    elif l2_y_distance == 0:
        l2_steps = abs(l2_x_distance) + 1
        l2_step_y = 0
        l2_step_x = 1 if d[0] > c[0] else -1
    else:
        l2_steps = abs(l2_x_distance) + 1
        l2_step_x = 1 if d[0] > c[0] else -1
        l2_step_y = 1 if d[1] > c[1] else -1

    res: dict = {}
    for l_step in range(min(l1_steps, l2_steps)):
            l1_x = a[0] + l1_step_x * l_step
            l1_y = a[1] + l1_step_y * l_step
            l2_x = c[0] + l2_step_x * l_step
            l2_y = c[1] + l2_step_y * l_step

            if l1_x == l2_x and l1_y == l2_y:
                res[l1_x, l1_y] = 1

    return res


def intersect_points_parallel_in_x(a, b, c, d):

    res: dict = {}
    denominator = float(((b[0] - a[0]) * (d[1] - c[1])) - ((b[1] - a[1]) * (d[0] - c[0])))

    if (denominator == 0):

        # are parallel lines in x?
        if (a[0] == b[0] == c[0] == d[0]):
            # normalize line
            line1 = (a[0], a[1], b[0], b[1]) if b[1] > a[1] else (b[0], b[1], a[0], a[1])
            line2 = (c[0], c[1], d[0], d[1]) if d[1] > c[1] else (d[0], d[1], c[0], c[1])

            if line2[1] < line1[1]:
                line1, line2 = line2, line1

            if line1[3] - line2[1] + 1 > 0:
                for y in range(line2[1], min(line1[3], line2[3]) + 1):
                    res[a[0], y] = 1
                return res
            else:
                return {}

    return {}

def intersect_points_parallel_in_y(a, b, c, d):

    res: dict = {}
    denominator = float(((b[0] - a[0]) * (d[1] - c[1])) - ((b[1] - a[1]) * (d[0] - c[0])))

    if (denominator == 0):

        # are parallel lines in y?
        if (a[1] == b[1] == c[1] == d[1]):
            # normalize line
            line1 = (a[0], a[1], b[0], b[1]) if b[0] > a[0] else (b[0], b[1], a[0], a[1])
            line2 = (c[0], c[1], d[0], d[1]) if d[0] > c[0] else (d[0], d[1], c[0], c[1])

            if line2[0] < line1[0]:
                line1, line2 = line2, line1

            if line1[2] - line2[0] + 1 > 0:
                for x in range(line2[0], min(line1[2], line2[2]) + 1):
                    res[x, a[1]] = 1
                return res
            else:
                return {}

    return {}

def intersect_points_parallel_in_diag(a, b, c, d):

    res: dict = {}
    denominator = float(((b[0] - a[0]) * (d[1] - c[1])) - ((b[1] - a[1]) * (d[0] - c[0])))
    numerator1 = float(((a[1] - c[1]) * (d[0] - c[0])) - ((a[0] - c[0]) * (d[1] - c[1])))
    numerator2 = float(((a[1] - c[1]) * (b[0] - a[0])) - ((a[0] - c[0]) * (b[1] - a[1])))

    expected = (185, 174)
    debug = True
    if a == expected or b == expected or c == expected or d == expected:
        debug = True

    # if (denominator == 0) and (numerator1 == 0 or numerator2 == 0):
    if (denominator == 0):

        # are parallel diagonal lines?
        if (a[0] + b[0] + c[0] + d[0] == a[1] + b[1] + c[1] + d[1]):
            min_x = sorted([a[0], b[0], c[0], d[0]])[1]
            max_x = sorted([a[0], b[0], c[0], d[0]])[2]
            min_y = sorted([a[1], b[1], c[1], d[1]])[1]
            max_y = sorted([a[1], b[1], c[1], d[1]])[2]

            if debug:
                print("are parallel diagonal lines?")
                # print("expected = (185, 174)")
                print(f"{a=}")
                print(f"{b=}")
                print(f"{c=}")
                print(f"{d=}")

                print(f"{min_x=}")
                print(f"{max_x=}")
                print(f"{min_y=}")
                print(f"{max_y=}")

            # for i in range(max_x - min_x + 1):
            #     res[(int(min_x + i), int(min_y + i))] = 1
            # return res

            for i in range(max_y - min_y + 1):
                res[(min_x + i), (min_y + i)] = 1
            if debug:
                # print(f"{res=}")
                input()
            return res

    return {}

def intersect(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # parallel
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return None
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return None
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return (x, y)

def intersect_points_others_new(a, b, c, d):
    res: dict = {}
    point = intersect(a, b, c, d)
    if point is None:
        return {}
    x = point[0]
    y = point[1]
    if abs(abs(x - int(x)) - 0.5) < 0.01:
        resx = int(x) + 0.5
        resy = int(y) + 0.5
    else:
        resx = int(round(x))
        resy = int(round(y))
    res[resx, resy] = 1
    return res


def intersect_points_others(a, b, c, d):
    res: dict = {}
    denominator = float(((b[0] - a[0]) * (d[1] - c[1])) - ((b[1] - a[1]) * (d[0] - c[0])))
    numerator1 = float(((a[1] - c[1]) * (d[0] - c[0])) - ((a[0] - c[0]) * (d[1] - c[1])))
    numerator2 = float(((a[1] - c[1]) * (b[0] - a[0])) - ((a[0] - c[0]) * (b[1] - a[1])))

    if (denominator != 0):

        r = numerator1 / denominator
        s = numerator2 / denominator
        if (r >= 0 and r <= 1) and (s >= 0 and s <= 1):
            x = a[0] + (r * (b[0] - a[0]))
            y = a[1] + (r * (b[1] - a[1]))
            # if x - int(x) == 0:
            #     return {}
            # print()
            # print("abcd:", a, b, c, d)
            # print("r:", r)
            # print("s:", s)
            # print("x:", x)
            # print("y:", y)
            if abs(abs(x - int(x)) - 0.5) < 0.01:
                # print("resx:", int(x) + 0.5, end=' ')
                # print("resy:", int(y) + 0.5, end=' ')
                resx = int(x) + 0.5
                resy = int(y) + 0.5
            else:
                # print("resx:", int(round(x)), end=' ')
                # print("resy:", int(round(y)), end=' ')
                resx = int(round(x))
                resy = int(round(y))
            # print()
            # input()
            res[resx, resy] = 1
            return res
    return {}

def is_point_on_and_between_line(x1, y1, x2, y2, x3, y3):

    slope = (y2 - y1) / (x2 - x1)
    pt3_on = (y3 - y1) == slope * (x3 - x1)
    pt3_between = (min(x1, x2) <= x3 <= max(x1, x2)) and (min(y1, y2) <= y3 <= max(y1, y2))
    on_and_between = pt3_on or pt3_between
    return on_and_between

def is_a_point(a, b):
    return a[0] == b[0] and a[1] == b[1]

def intersect_points_in_the_line(a, b, c, d):
    res: dict = {}
    if is_a_point(a, b):
        if is_point_on_and_between_line(c[0], c[1], d[0], d[1], a[0], a[1]):
            res[a[0], a[1]] = 1
            return res
    if is_a_point(c, d):
        if is_point_on_and_between_line(a[0], a[1], b[0], b[1], c[0], c[1]):
            res[c[0], c[1]] = 1
            return res
    return {}


def intersect_only_points(a, b, c, d):
    res: dict = {}
    if (((a[0] == b[0]) == c[0]) == d[0]) and (((a[1] == b[1]) == c[1]) == d[1]):
        res[a[0], a[1]] = 1
        return res
    return {}

def intersect_points(a, b, c, d):
    """
             intersect_points(a, b, c, d)

             line1 = a --- b
             line2 = c --- d

             float uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
             float uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
                         ((d[0] - c[0]) * (a[1] - c[1]) - (d[1] - c[1]))*(a[0] - c[0])/
                         ((d[1] - c[1]*(b[0] - a[0]) - (d[0] - c[0])*(b[1] - a[1])))
    """
    res: dict = {}
    # print("x     :", len(intersect_points_parallel_in_x(a, b, c, d)))
    # print("y     :", len(intersect_points_parallel_in_y(a, b, c, d)))
    # print("diag  :", len(intersect_points_parallel_in_diag(a, b, c, d)))
    # print("others:", len(intersect_points_others(a, b, c, d)))

    # res = {**dict(res), **dict(intersect_points_parallel_in_x(a, b, c, d))}
    # res = {**dict(res), **dict(intersect_points_parallel_in_y(a, b, c, d))}
    # # res = {**dict(res), **dict(intersect_points_parallel_in_diag(a, b, c, d))}
    # # res = {**dict(res), **dict(intersect_points_others(a, b, c, d))}

    res = res | intersect_points_parallel_in_x(a, b, c, d)
    res = res | intersect_points_parallel_in_y(a, b, c, d)
    res = res | intersect_points_parallel_in_diag(a, b, c, d)
    res = res | intersect_points_others_new(a, b, c, d)
    res = res | intersect_only_points(a, b, c, d)
    res = res | intersect_points_in_the_line(a, b, c, d)
    return res

def is_line_horizontal_or_vertical(a, b):
    return True if (a[0] == b[0] or a[1] == b[1]) else False

def are_lines_horizontal_or_vertical(a, b, c, d):
    return is_line_horizontal_or_vertical(a, b) and is_line_horizontal_or_vertical(c, d)

def init_data(input_file):

    for line in input_file:
        m = re.search(r"(\d*),(\d*)\D+(\d*),(\d*)", line)
        a = (int(m.group(1)), int(m.group(2)))
        b = (int(m.group(3)), int(m.group(4)))
        PuzzleData.lines.append((a, b))
    debug_print(PuzzleData.lines)
    print_yellow("init data...", end="\n")

# ------------- LOAD FILE --------------

def load_input_file():
    file = "input.txt" if not __debug__ else 'test.txt'
    with open(file, 'r') as reader:
        input_file = [i.rstrip("\n") for i in reader.readlines()]
    if len(input_file) == 0:
        assert False
    print_yellow("load file...", end="\n")
    return input_file

def write_dots(diagram={}, dot=''):
    if diagram.get(dot):
        diagram[dot] += 1
    else:
        diagram[dot] = 1

def write_line(diagram={}, dot1='', dot2=''):
    x1, y1 = map(int, dot1.split(','))
    x2, y2 = map(int, dot2.split(','))
    if x1 == x2 and y1 == y2:
        # just dot
        write_dots(diagram, dot1)
    elif x1 == x2:
        # horizontal lines
        p1, p2, step = get_range(y1, y2)
        for y in range(p1, p2, step):
            write_dots(diagram, f'{x1},{y}')
    elif y1 == y2:
        # vertical lines
        p1, p2, step = get_range(x1, x2)
        for x in range(p1, p2, step):
            write_dots(diagram, f'{x},{y1}')
    elif abs(x1 - x2) == abs(y1 - y2):
        # diagonal lines
        px1, px2, step_x = get_range(x1, x2)
        _, _, step_y = get_range(y1, y2)
        for _ in range(px1, px2, step_x):
            write_dots(diagram, f'{x1},{y1}')
            x1 += step_x
            y1 += step_y
    else:
        # another type of lines
        pass

def get_range(p1, p2):
    if p1 > p2:
        step = -1
        p2 -= 1
    else:
        step = 1
        p2 += 1
    return p1, p2, step

# ------------- MAIN METHOD --------------

sum = 0


def main():

    init_data(load_input_file())

    intersect_points_part1: dict = {}
    intersect_points_part2: dict = {}

    points_parallel_in_x: dict = {}
    points_parallel_in_y: dict = {}
    points_parallel_in_diag: dict = {}
    points_others: dict = {}
    points_only: dict = {}
    points_in_line: dict = {}

    points: dict = {}

    print("=== writing points ===")
    with open("input.txt") as f:
        for line in f:
            dot1, dot2 = line.replace('\n', '').split(' -> ')
            write_line(points, dot1, dot2)

    # sum = 0
    # for point, count in points.items():
    #
    #     i_am_tuple = tuple(map(int, point.split(',')))
    #     print(f"{i_am_tuple=}")
    #     input()
    #     if count > 1:
    #         sum += 1
    # print(f"{sum=}")
    # input()

    print("=== writing intersections ===")

    # iterate over all lines but last (line1 set) ...
    for i, line1 in enumerate(PuzzleData.lines[:-1]):
        #   ... iterate over subset of all lines from line1 [i]
        for line2 in PuzzleData.lines[i + 1:]:

            # intersect_points_part1 = {**intersect_points_part1, **dict(intersect_points_new(line1[0], line1[1], line2[0], line2[1]) if are_lines_horizontal_or_vertical(line1[0], line1[1], line2[0], line2[1]) else {})}
            # intersect_points_part2 = {**intersect_points_part2, **dict(intersect_points_new(line1[0], line1[1], line2[0], line2[1]))}
            if are_lines_horizontal_or_vertical(line1[0], line1[1], line2[0], line2[1]):
                intersect_points_part1 = {**intersect_points_part1, **dict(intersect_points(line1[0], line1[1], line2[0], line2[1]))}
            intersect_points_part2 = {**intersect_points_part2, **dict(intersect_points(line1[0], line1[1], line2[0], line2[1]))}
            # # input()
            # if are_lines_horizontal_or_vertical(line1[0], line1[1], line2[0], line2[1]):
            # points_parallel_in_x = {**points_parallel_in_x, **dict(intersect_points_parallel_in_x(line1[0], line1[1], line2[0], line2[1]))}
            # points_parallel_in_y = {**points_parallel_in_y, **dict(intersect_points_parallel_in_y(line1[0], line1[1], line2[0], line2[1]))}
            # points_parallel_in_diag = {**points_parallel_in_diag, **dict(intersect_points_parallel_in_diag(line1[0], line1[1], line2[0], line2[1]))}
            # points_others = {**points_others, **dict(intersect_points_others(line1[0], line1[1], line2[0], line2[1]))}
            # points_only = {**points_only, **dict(intersect_only_points(line1[0], line1[1], line2[0], line2[1]))}
            # points_in_line = {**points_in_line, **dict(intersect_points_in_the_line(line1[0], line1[1], line2[0], line2[1]))}
    #
    intersect_points_part2 = intersect_points_part2 | intersect_points_part1

    # with open('test_part1.txt', 'w') as f:
    #     f.write(str(intersect_points_part2))
    #
    # with open('test_xy.txt', 'w') as f:
    #     f.write(str(points_parallel_in_x))
    #     f.write(str(points_parallel_in_y))

    print("part1:", len(intersect_points_part1))
    print("part2:", len(intersect_points_part2))

    print("points part2:", len(list(points.values())) - list(points.values()).count(1))

    sum = 0

    with open('test_points.txt', 'w') as f:
        for point, count in points.items():
            if count > 1:
                i_am_tuple = tuple(map(int, point.split(',')))
                if i_am_tuple not in intersect_points_part2:
                    f.write(str(i_am_tuple) + '=' + str(count) + '\n')
                # print(point, " = ", count)
                # input()

    with open('test_intersections.txt', 'w') as f:
        for point, count in intersect_points_part2.items():
            i_am_str = str(str(point[0]) + ',' + str(point[1]))
            if i_am_str not in points:
                f.write(str(i_am_str) + '=' + str(count) + '\n')

    print(sum)

    # print("points_parallel_in_x:", len(points_parallel_in_x))
    # print("points_parallel_in_y:", len(points_parallel_in_y))
    # print("points_parallel_in_diag:", len(points_parallel_in_diag))
    # print("points_others:", len(points_others))
    # print("points_only:", len(points_only))
    # print("points_in_line:", len(points_in_line))

def test():

    intersect_points_new((1, 1),(5, 5),(5, 5),(1, 1))
    intersect_points_new((5, 5),(1, 1),(5, 5),(1, 1))
    intersect_points_new((1, 5),(1, 1),(5, 5),(1, 1))


# ------------- MAIN --------------

if __name__ == '__main__':
    main()
