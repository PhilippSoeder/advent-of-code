'''
Advent of Code 2023 - Day 21
'''
import aocd


def solve_a(step_goal):
    seen = set()
    seen.add(start)
    while step_goal > 0:
        step_goal -= 1
        tmp = set()
        for r, c in seen:
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
                    if grid[r + dr][c + dc] != "#":
                        tmp.add((r + dr, c + dc))
        seen = tmp
    return len(seen)


def solve_b(step_goal):
    # only solved after lots of googling, multiple videos
    # and the solution megathread on reddit :(
    # best explanation: https://www.youtube.com/watch?v=9UOMZSL0JTg

    # Assumptions that the grid is a square
    assert len(grid) == len(grid[0])
    size = len(grid)

    # Assumption that the starting point is in the middle of the grid
    assert start == (size // 2, size // 2)

    # Assumption that after the step_goal we reach the edge of a grid and
    # travel x times a full grid + half of a grid (initial grid) in the end
    assert step_goal % size == size // 2

    grid_width = step_goal // size - 1

    sr, sc = start

    # those numbers of points can be reached in an even/odd grid
    odd = (grid_width // 2 * 2 + 1) ** 2
    even = ((grid_width + 1) // 2 * 2) ** 2
    odd_points = fill(sr, sc, size * 2 + 1)
    even_points = fill(sr, sc, size * 2)

    # corners of the grid are not filled completely (two edges missing)
    corner_t = fill(size - 1, sc, size - 1)
    corner_r = fill(sr, 0, size - 1)
    corner_b = fill(0, sc, size - 1)
    corner_l = fill(sr, size - 1, size - 1)
    corners = corner_t + corner_r + corner_b + corner_l

    # small segments on the side
    small_tr = fill(size - 1, 0, size // 2 - 1)
    small_tl = fill(size - 1, size - 1, size // 2 - 1)
    small_br = fill(0, 0, size // 2 - 1)
    small_bl = fill(0, size - 1, size // 2 - 1)
    small = small_tr + small_tl + small_br + small_bl

    # large segements on the side
    large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
    large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
    large_br = fill(0, 0, size * 3 // 2 - 1)
    large_bl = fill(0, size - 1, size * 3 // 2 - 1)
    large = large_tr + large_tl + large_br + large_bl

    result = odd * odd_points
    result += even * even_points
    result += corners
    result += (grid_width + 1) * small
    result += grid_width * large
    return result


def fill(sr, sc, ss):
    # belongs to part b
    # also inspired by https://www.youtube.com/watch?v=9UOMZSL0JTg
    result = set()
    seen = {(sr, sc)}
    q = [(sr, sc, ss)]
    while len(q) > 0:
        r, c, s = q.pop(0)
        if s % 2 == 0:
            result.add((r, c))
        if s == 0:
            continue
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) \
               and grid[nr][nc] != "#" and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, s - 1))
    return len(result)


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 21
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = []
    for line in input:
        grid.append([x for x in line])

    for r, row in enumerate(grid):
        for c, element in enumerate(row):
            if element == "S":
                start = (r, c)

    part_a = solve_a(64)
    part_b = solve_b(26501365)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
