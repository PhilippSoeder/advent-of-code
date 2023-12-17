'''
Advent of Code 2023 - Day 17
'''
import aocd
from heapq import heappush, heappop
import plotly.express as px


def find_shortest_path(grid, part):
    destination = (len(grid) - 1, len(grid[0]) - 1)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen = set()
    q = [(0, 0, 0, 0, 0, 0)]
    match part:
        case "a":
            min_d_cnt = 1
            max_d_cnt = 3
        case "b":
            min_d_cnt = 4
            max_d_cnt = 10

    while len(q) > 0:
        cost, r, c, dr, dc, d_cnt = heappop(q)

        if (r, c) == destination and d_cnt >= min_d_cnt:
            return cost

        if (r, c, dr, dc, d_cnt) in seen:
            continue
        seen.add((r, c, dr, dc, d_cnt))

        if d_cnt < max_d_cnt:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(q, (cost + grid[nr][nc], nr, nc, dr, dc, d_cnt + 1))
        if d_cnt >= min_d_cnt or (dr, dc) == (0, 0):
            for ndr, ndc in directions:
                if (ndr, ndc) != (-dr, -dc) and (ndr, ndc) != (dr, dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        heat_loss_new = cost + grid[nr][nc]
                        heappush(q, (heat_loss_new, nr, nc, ndr, ndc, 1))


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 17
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = [list(map(int, line)) for line in input]

    part_a = find_shortest_path(grid, "a")
    part_b = find_shortest_path(grid, "b")

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)

    # not needed for solution, but nice visualization ;)
    heatmap = px.imshow(grid)
    heatmap.show()
