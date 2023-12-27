'''
Advent of Code 2021 - Day 11
'''
import aocd


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 11
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0

    grid = [[int(ch) for ch in line] for line in input]

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    step = 0
    while True:
        step += 1
        grid = [[n + 1 for n in row] for row in grid]
        flashed = set()
        q = []
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] > 9:
                    q.append((r, c))
        while len(q) > 0:
            r, c = q.pop(0)
            if (r, c) in flashed:
                continue
            grid[r][c] += 1
            if grid[r][c] > 9:
                flashed.add((r, c))
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        q.append((nr, nc))
        for (r, c) in flashed:
            grid[r][c] = 0
        if step <= 100:
            part_a += len(flashed)
        if len(flashed) == len(grid) * len(grid[0]):
            part_b = step
            break

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
