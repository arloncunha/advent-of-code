# --- Day 11: Seating System ---
# https://adventofcode.com/2020/day/11

def count_occupied():
    count = 0
    for i in range(rows):
        for j in range(cols):
            count = count + has_seat(i, j)
    return count


def position(i, j):
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return ' '
    else:
        return board[i][j]
    # try:
    #     return input[i][j]
    # except:  # noqa: E722
    #     return ' '


def has_seat(i, j):
    if position(i, j) == '#':
        # print(i, j, "has seat")
        return True
    else:
        return False


def has_seat_dir(i, j, dir_x, dir_y):
    has = False
    skip = False

    x = i
    y = j
    while not skip and not has:
        x = x + dir_x
        y = y + dir_y
        has = has_seat(x, y)
        if position(x, y) == 'L' or position(x, y) == ' ':
            skip = True
    return has


def no_occupied_seats(i, j):
    if not has_seat(i - 1, j - 1) and \
       not has_seat(i - 1, j) and \
       not has_seat(i - 1, j + 1) and \
       not has_seat(i, j - 1) and \
       not has_seat(i, j) and \
       not has_seat(i, j + 1) and \
       not has_seat(i + 1, j - 1) and \
       not has_seat(i + 1, j) and \
       not has_seat(i + 1, j + 1):
        return True
    else:
        return False


def no_occupied_seats_dir(i, j):

    if not has_seat_dir(i, j, - 1, - 1) and \
       not has_seat_dir(i, j, - 1, 0) and \
       not has_seat_dir(i, j, - 1, + 1) and \
       not has_seat_dir(i, j, + 1, - 1) and \
       not has_seat_dir(i, j, + 1, 0) and \
       not has_seat_dir(i, j, + 1, + 1) and \
       not has_seat_dir(i, j, 0, - 1) and \
       not has_seat_dir(i, j, 0, + 1):
        return True
    else:
        return False


def ge_four_occupied_seats(i, j):

    occupied = 0
    if has_seat(i - 1, j - 1):
        occupied = occupied + 1
    if has_seat(i - 1, j):
        occupied = occupied + 1
    if has_seat(i - 1, j + 1):
        occupied = occupied + 1
    if has_seat(i, j - 1):
        occupied = occupied + 1
    if has_seat(i, j + 1):
        occupied = occupied + 1
    if has_seat(i + 1, j - 1):
        occupied = occupied + 1
    if has_seat(i + 1, j):
        occupied = occupied + 1
    if has_seat(i + 1, j + 1):
        occupied = occupied + 1

    if occupied >= 4:
        return True
    else:
        return False


def ge_five_occupied_seats(i, j):

    occupied = 0
    if has_seat_dir(i, j, - 1, - 1):
        occupied = occupied + 1
    if has_seat_dir(i, j, - 1, 0):
        occupied = occupied + 1
    if has_seat_dir(i, j, - 1, + 1):
        occupied = occupied + 1
    if has_seat_dir(i, j, 1, - 1):
        occupied = occupied + 1
    if has_seat_dir(i, j, 1, 0):
        occupied = occupied + 1
    if has_seat_dir(i, j, 1, + 1):
        occupied = occupied + 1
    if has_seat_dir(i, j, 0, - 1):
        occupied = occupied + 1
    if has_seat_dir(i, j, 0, + 1):
        occupied = occupied + 1

    if occupied >= 5:
        return True
    else:
        return False


with open('input.txt', 'r') as reader:
    input = [list(i.strip()) for i in reader.readlines()]

rows = len(input)
cols = len(input[0])

round = 0
board = input.copy()
while True:
    new_board = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if position(i, j) == 'L' and no_occupied_seats(i, j):
                new_board[i][j] = '#'
            elif position(i, j) == '#' and ge_four_occupied_seats(i, j):
                new_board[i][j] = 'L'
            else:
                new_board[i][j] = board[i][j]
    if board == new_board:
        break
    board = new_board.copy()
print(count_occupied())

board = input.copy()
while True:
    new_board = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if position(i, j) == 'L' and no_occupied_seats_dir(i, j):
                new_board[i][j] = '#'
            elif position(i, j) == '#' and ge_five_occupied_seats(i, j):
                new_board[i][j] = 'L'
            else:
                new_board[i][j] = board[i][j]
    if board == new_board:
        break
    board = new_board.copy()
print(count_occupied())
