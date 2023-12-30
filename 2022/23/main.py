'''
Advent of Code 2022 - Day 23
'''
import aocd
import sys


def count_empty():
    t = 0
    min_r = sys.maxsize
    max_r = 0
    min_c = sys.maxsize
    max_c = 0
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if grid[r][c] == '#':
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if grid[r][c] == '.':
                t += 1
    return t


def is_elve_adjacent(elve):
    global directions
    for d in directions:
        for e in d:
            if grid[elve[0]+e[0]][elve[1]+e[1]] == '#':
                return True
    return False


def get_next_position(elve):
    for direction in directions:
        valid = True
        for d in direction:
            if grid[elve[0]+d[0]][elve[1]+d[1]] == '#':
                valid = False
        if valid:
            return (elve[0]+direction[0][0], elve[1]+direction[0][1])
    return (elve[0], elve[1])


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 23
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = []
    for r, row in enumerate(input):
        move_to_point_count = []
        for c, column in enumerate(row):
            move_to_point_count.append(column)
        grid.append(move_to_point_count)
    row_count = len(grid)
    column_count = len(grid[0])
    for _ in range(row_count*3):
        grid.insert(0, ['.' for _ in range(column_count*3)])
    for r in range(row_count*3, row_count*4):
        for _ in range(column_count):
            grid[r].insert(0, '.')
        for _ in range(column_count):
            grid[r].append('.')
    for _ in range(row_count*3):
        grid.append(['.' for _ in range(column_count*3)])

    directions = [
        [(-1, 0), (-1, 1), (-1, -1)],
        [(1, 0), (1, 1), (1, -1)],
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (-1, 1), (1, 1)]
    ]

    i = 0
    moved = True
    while moved:
        moved = False
        elves = []
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == '#':
                    elves.append([r, c])

        needs_to_move = []
        for elve in elves:
            if is_elve_adjacent(elve):
                needs_to_move.append(elve)

        moves = []
        for elve in needs_to_move:
            moves.append([elve, get_next_position(elve)])

        move_to_point_count = {}
        for m in moves:
            if m[1] in move_to_point_count:
                move_to_point_count[m[1]] += 1
            else:
                move_to_point_count[m[1]] = 1

        valid_moves = []
        for move in moves:
            if move_to_point_count[move[1]] == 1:
                valid_moves.append(move)

        for v in valid_moves:
            moved = True
            grid[v[0][0]][v[0][1]] = '.'
            grid[v[1][0]][v[1][1]] = '#'

        directions.append(directions.pop(0))
        i += 1

        if i == 10:
            part1 = count_empty()

    part2 = i

    print(f'{part1 = }')
    print(f'{part2 = }')

    aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
