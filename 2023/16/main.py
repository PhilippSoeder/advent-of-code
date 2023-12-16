'''
Advent of Code 2023 - Day 16
'''
import aocd


def solve(start):
    positions = [start]
    seen = set()
    energized = set()

    while len(positions) > 0:
        p = 0
        r, c = positions[p][:2]
        dr, dc = positions[p][2:]

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[p]) \
           or positions[p] in seen:
            positions.pop(p)
            continue
        else:
            seen.add(positions[p])
            energized.add((r, c))

        tile = grid[r][c]
        match tile:
            case ".":
                positions[p] = (r + dr, c + dc, dr, dc)
            case "/":
                if (dr, dc) == (0, 1):
                    positions[p] = (r - 1, c, -1, 0)
                elif (dr, dc) == (0, -1):
                    positions[p] = (r + 1, c, 1, 0)
                elif (dr, dc) == (1, 0):
                    positions[p] = (r, c - 1, 0, -1)
                elif (dr, dc) == (-1, 0):
                    positions[p] = (r, c + 1, 0, 1)
            case "\\":
                if (dr, dc) == (0, 1):
                    positions[p] = (r + 1, c, 1, 0)
                elif (dr, dc) == (0, -1):
                    positions[p] = (r - 1, c, -1, 0)
                elif (dr, dc) == (1, 0):
                    positions[p] = (r, c + 1, 0, 1)
                elif (dr, dc) == (-1, 0):
                    positions[p] = (r, c - 1, 0, -1)
            case "|":
                if (dr, dc) in [(0, 1), (0, -1)]:
                    positions[p] = (r - 1, c, -1, 0)
                    positions.append((r + 1, c, 1, 0))
                else:
                    positions[p] = (r + dr, c + dc, dr, dc)
            case "-":
                if (dr, dc) in [(1, 0), (-1, 0)]:
                    positions[p] = (r, c - 1, 0, -1)
                    positions.append((r, c + 1, 0, 1))
                else:
                    positions[p] = (r + dr, c + dc, dr, dc)
    return len(energized)


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 16
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = []
    for line in input:
        grid.append([x for x in line])

    part_a = solve((0, 0, 0, 1))

    starting_positions_b = []
    for r in range(len(grid)):
        starting_positions_b.append((r, 0, 0, 1))
        starting_positions_b.append((r, len(grid[0])-1, 0, -1))
    for c in range(len(grid[0])):
        starting_positions_b.append((0, c, 1, 0))
        starting_positions_b.append((len(grid)-1, c, -1, 0))
    part_b = max([solve(p) for p in starting_positions_b])

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
