'''
Advent of Code 2023 - Day 14
'''
import aocd


def roll(grid):
    grid = list(map(list, zip(*grid)))
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            pos = c
            if grid[r][c] == "O" and c > 0:
                for i in range(c - 1, -1, -1):
                    if grid[r][i] == ".":
                        grid[r][i] = "O"
                        grid[r][pos] = "."
                        pos -= pos - i
                    elif grid[r][i] == "#":
                        break
    grid = list(map(list, zip(*grid)))
    return grid


def rotate(grid):
    result = [['.' for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            result[c][len(grid) - 1 - r] = grid[r][c]
    return result


def get_load(grid):
    result = 0
    for r, row in enumerate(grid):
        result += (len(grid) - r) * row.count('O')
    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 14
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = []
    for line in input:
        grid.append([x for x in line])

    seen = {}
    goal = 1000000000
    cnt = 0
    while cnt < goal:
        cnt += 1
        for d in range(4):
            grid = roll(grid)
            if cnt == 1 and d == 0:
                part_a = get_load(grid)
            grid = rotate(grid)
        state = tuple(tuple(row) for row in grid)
        if state in seen:
            cnt += ((goal - cnt) // (cnt - seen[state])) * (cnt - seen[state])
        else:
            seen[state] = cnt
    part_b = get_load(grid)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
