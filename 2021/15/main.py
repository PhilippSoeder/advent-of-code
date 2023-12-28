'''
Advent of Code 2023 - Day 15
'''
import aocd
from heapq import heappush, heappop


def solve(n):
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    D = [[None for _ in range(n * len(grid[0]))] for _ in range(n * len(grid))]
    q = [(0, 0, 0)]
    while len(q) > 0:
        (cost, r, c) = heappop(q)
        if r < 0 or r >= n * len(grid) or c < 0 or c >= n * len(grid[0]):
            continue

        val = grid[r % len(grid)][c % len(grid[0])] \
            + (r // len(grid)) + (c // len(grid[0]))
        while val > 9:
            val -= 9
        rc_cost = cost + val

        if D[r][c] is None or rc_cost < D[r][c]:
            D[r][c] = rc_cost
        else:
            continue
        if r == n * len(grid) - 1 and c == n * len(grid[0]) - 1:
            break

        for (dr, dc) in directions:
            nr = r + dr
            nc = c + dc
            heappush(q, ((D[r][c], nr, nc)))
    return D[n * len(grid) - 1][n * len(grid[0]) - 1] - grid[0][0]


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 15
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = [list(map(int, line)) for line in input]

    part_a = solve(1)
    part_b = solve(5)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
