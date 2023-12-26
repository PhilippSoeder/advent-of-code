'''
Advent of Code 2021 - Day 9
'''
import aocd


def solve_a(grid):
    result = 0
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            for (dr, dc) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= r + dr < len(grid) and 0 <= c + dc < len(row):
                    if grid[r][c] >= grid[r + dr][c + dc]:
                        break
            else:
                result += grid[r][c] + 1
    return result


def solve_b(grid):
    basins = []
    seen = set()
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            size = 0
            q = [(r, c)]
            while len(q) > 0:
                r, c = q.pop(0)
                if (r, c) in seen:
                    continue
                seen.add((r, c))
                if grid[r][c] != 9:
                    size += 1
                    for (dr, dc) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(row):
                            if grid[r + dr][c + dc] != 9:
                                q.append((r + dr, c + dc))
            basins.append(size)
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 9
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = [[int(x) for x in line] for line in input]

    part_a = solve_a(grid)
    part_b = solve_b(grid)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
