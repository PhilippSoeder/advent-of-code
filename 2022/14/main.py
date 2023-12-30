'''
Advent of Code 2022 - Day 14
'''
import aocd
import sys


def create_grid(part2):
    grid = []
    extra_x = max_y
    for _ in range(0, max_y+1):
        row = []
        for _ in range(min_x - extra_x, max_x+1+extra_x):
            row.append('.')
        grid.append(row)

    if part2:
        paths.append([(min_x-extra_x, max_y), (max_x+extra_x, max_y)])

    for p, path in enumerate(paths):
        for i in range(len(path)-1):
            x1 = paths[p][i][0] - min_x + extra_x
            x2 = paths[p][i+1][0] - min_x + extra_x
            if x1 > x2:
                x1, x2 = x2, x1
            y1 = paths[p][i][1]
            y2 = paths[p][i+1][1]
            if y1 > y2:
                y1, y2 = y2, y1
            if x1 == x2:
                for i in range(y1, y2+1):
                    grid[i][x1] = '#'
            elif y1 == y2:
                for i in range(x1, x2+1):
                    grid[y1][i] = '#'
    s = (500-min_x + extra_x, 0)
    grid[s[1]][s[0]] = '+'
    return grid, s


def sand_flow(grid, p, part2):
    if p[1]+1 > max_y:
        if part2:
            return
        return 0
    if grid[p[1]+1][p[0]] != '#' and grid[p[1]+1][p[0]] != 'o':
        return sand_flow(grid, (p[0], p[1]+1), part2)
    else:
        if grid[p[1]+1][p[0]-1] != '#' and grid[p[1]+1][p[0]-1] != 'o':
            return sand_flow(grid, (p[0]-1, p[1]+1), part2)
        elif grid[p[1]+1][p[0]+1] != '#' and grid[p[1]+1][p[0]+1] != 'o':
            return sand_flow(grid, (p[0]+1, p[1]+1), part2)
        else:
            grid[p[1]][p[0]] = 'o'
            if part2 and p == s:
                return 0


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 14
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    paths = []
    for line in input:
        points = line.split(' -> ')
        for p, point in enumerate(points):
            x, y = point.split(',')
            points[p] = (int(x), int(y))
        paths.append(points)

    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = 0
    max_y = 0

    for path in paths:
        for point in path:
            if min_x > point[0]:
                min_x = point[0]
            if min_y > point[1]:
                min_y = point[1]
            if max_x < point[0]:
                max_x = point[0]
            if max_y < point[1]:
                max_y = point[1]

    # Part 1
    grid, s = create_grid(part2=False)
    a = 0
    while sand_flow(grid, s, part2=False) != 0:
        a += 1
    print(f'{a = }')

    # Part 2
    max_y += 2
    grid, s = create_grid(part2=True)
    b = 1
    while sand_flow(grid, s, part2=True) != 0:
        b += 1
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
