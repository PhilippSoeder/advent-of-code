'''
Advent of Code 2021 - Day 4
'''
import aocd


def is_win(board, numbers):
    if len(numbers) < 5:
        return False
    for line in board:
        if set(line) <= set(numbers):
            return True
    for i in range(len(board[0])-1):
        column = []
        for line in board:
            column.append(line[i])
        if set(column) <= set(numbers):
            return True
    return False


def calculate_result(board, numbers):
    uncalled = []
    for line in board:
        for n in line:
            if n not in numbers:
                uncalled.append(n)
    return sum(uncalled) * numbers[-1]


AOC_YEAR = 2021
AOC_DAY = 4
input = open("input.txt").read().split('\n\n')
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).split('\n\n')
numbers = list(map(int, input[0].split(',')))
boards = []
for line in input[1:]:
    board = line.split('\n')
    b = []
    for ln in board:
        b.append(list(map(int, ln.split())))
    boards.append(b)

boards_won = []
for n, _ in enumerate(numbers):
    for i, b in enumerate(boards):
        if is_win(b, numbers[:n]) and b not in boards_won:
            if len(boards_won) == 0:
                part1 = calculate_result(b, numbers[:n])
            boards_won.append(b)
            if len(boards_won) == len(boards):
                part2 = calculate_result(b, numbers[:n])

print(f'{part1 = }')
print(f'{part2 = }')
aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
