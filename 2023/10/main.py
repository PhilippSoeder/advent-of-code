'''
Advent of Code 2023 - Day 10
'''
import aocd


def find_start(grid):
    for r, row in enumerate(grid):
        for c, pipe in enumerate(row):
            if pipe == "S":
                return (r, c)


def find_next(g, c, p):
    for nr in (-1, 0, 1):
        for nc in (-1, 0, 1):
            if c[0] + nr >= 0 and c[0] + nr < len(g) \
               and c[1] + nc >= 0 and c[1] + nc < len(g[0]) \
               and not (c[0] + nr, c[1] + nc) == p:
                match (nr, nc):
                    case (-1, 0):  # north
                        if g[c[0] + nr][c[1] + nc] in ["|", "F", "7", "S"] \
                           and g[c[0]][c[1]] in ["S", "|", "L", "J"]:
                            return (c[0] + nr, c[1] + nc)
                    case (0, 1):  # east
                        if g[c[0] + nr][c[1] + nc] in ["-", "7", "J", "S"] \
                           and g[c[0]][c[1]] in ["S", "-", "L", "F"]:
                            return (c[0] + nr, c[1] + nc)
                    case (1, 0):  # south
                        if g[c[0] + nr][c[1] + nc] in ["|", "L", "J", "S"] \
                           and g[c[0]][c[1]] in ["S", "|", "7", "F"]:
                            return (c[0] + nr, c[1] + nc)
                    case (0, -1):  # west
                        if g[c[0] + nr][c[1] + nc] in ["-", "L", "F", "S"] \
                           and g[c[0]][c[1]] in ["S", "-", "J", "7"]:
                            return (c[0] + nr, c[1] + nc)


def replace_s(grid, path, start):
    end1 = path[0]
    end2 = path[-1]
    a = (end1[0] - start[0], end1[1] - start[1])
    b = (end2[0] - start[0], end2[1] - start[1])
    match (a, b):
        case ((-1, 0), (1, 0)) | ((1, 0), (-1, 0)):
            grid[start[0]][start[1]] = "|"
        case ((0, -1), (0, 1)) | ((0, 1), (0, -1)):
            grid[start[0]][start[1]] = "-"
        case ((-1, 0), (0, 1)) | ((0, 1), (-1, 0)):
            grid[start[0]][start[1]] = "L"
        case ((-1, 0), (0, -1)) | ((0, -1), (-1, 0)):
            grid[start[0]][start[1]] = "J"
        case ((1, 0), (0, -1)) | ((0, -1), (1, 0)):
            grid[start[0]][start[1]] = "7"
        case ((1, 0), (0, 1)) | ((0, 1), (1, 0)):
            grid[start[0]][start[1]] = "F"


def remove_non_path(grid, path):
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if not (r, c) in path:
                grid[r][c] = "."


def create_bigger_grid(grid):
    bigger_grid = []
    for row in grid:
        row_new1 = []
        row_new2 = []
        for c, pipe in enumerate(row):
            row_new1.append(pipe)
            match pipe:
                case "|" | "7":
                    row_new1.append(".")
                    row_new2.append("|")
                case "." | "J":
                    row_new1.append(".")
                    row_new2.append(".")
                case "-" | "L":
                    row_new1.append("-")
                    row_new2.append(".")
                case "F":
                    row_new1.append("-")
                    row_new2.append("|")
            row_new2.append(".")
        bigger_grid.append(row_new1)
        bigger_grid.append(row_new2)
    return bigger_grid


def get_initial_to_visit(bigger_grid):
    to_visit = []
    for i in range(len(bigger_grid[0])):
        to_visit.append((0, i))
        to_visit.append((len(bigger_grid)-1, i))
    for i in range(1, len(bigger_grid)-1):
        to_visit.append((i, 0))
        to_visit.append((i, len(bigger_grid[0])-1))
    return to_visit


def shrink_grid(bigger_grid):
    smaller_grid = []
    for r, row in enumerate(bigger_grid):
        if r % 2 == 0:
            smaller_grid.append([x for i, x in enumerate(row) if i % 2 == 0])
    return smaller_grid


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 10
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0

    grid = []
    path = []

    for line in input:
        row = [x for x in line]
        grid.append(row)

    start = find_start(grid)
    position = start
    previous = (-1, -1)

    while True:
        current = find_next(grid, position, previous)
        previous = position
        position = current
        if current == start:
            break
        path.append(position)

    part_a = len(path) // 2 + 1

    # part b
    replace_s(grid, path, start)
    path.append(start)
    remove_non_path(grid, path)
    bigger_grid = create_bigger_grid(grid)

    visited = set()
    to_visit = get_initial_to_visit(bigger_grid)

    while len(to_visit) > 0:
        current = to_visit.pop(0)
        visited.add(current)
        if bigger_grid[current[0]][current[1]] == ".":
            bigger_grid[current[0]][current[1]] = "0"
        else:
            continue
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if not i == j:
                    next = (current[0] + i, current[1] + j)
                    if next[0] >= 0 and next[0] < len(bigger_grid) \
                       and next[1] >= 0 and next[1] < len(bigger_grid[0]) \
                       and not next == current and next not in visited \
                       and next not in to_visit \
                       and bigger_grid[next[0]][next[1]] == ".":
                        to_visit.append(next)

    grid = shrink_grid(bigger_grid)

    for row in grid:
        part_b += row.count(".")

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
