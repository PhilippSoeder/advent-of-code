'''
Advent of Code 2022 - Day 14
'''
import aocd
import sys


def part1():
    grid = []
    for _ in range(0, max_y+1):
        row = []
        for _ in range(min_x, max_x+1):
            row.append('.')
        grid.append(row)

    for p, path in enumerate(paths):
        for i in range(len(path)-1):
            x1 = paths[p][i][0] - min_x
            x2 = paths[p][i+1][0] - min_x
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

    s = (500-min_x, 0)
    grid[s[1]][s[0]] = '+'

    a = 0
    while sand_fall(grid, s, 0) is None:
        a += 1
    return a


def part2():
    grid = []
    extra_x = max_y
    for _ in range(0, max_y+1):
        row = []
        for _ in range(min_x - extra_x, max_x+1+extra_x):
            row.append('.')
        grid.append(row)

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

    a = 0
    while sand_fall2(grid, s, 0, s) is None:
        a += 1
    return a


def sand_fall(grid, p, a):
    if p[1]+1 > max_y:
        return a
    if grid[p[1]+1][p[0]] != '#' and grid[p[1]+1][p[0]] != 'o':
        return sand_fall(grid, (p[0], p[1]+1), a)
    else:
        if grid[p[1]+1][p[0]-1] != '#' and grid[p[1]+1][p[0]-1] != 'o':
            return sand_fall(grid, (p[0]-1, p[1]+1), a)
        elif grid[p[1]+1][p[0]+1] != '#' and grid[p[1]+1][p[0]+1] != 'o':
            return sand_fall(grid, (p[0]+1, p[1]+1), a)
        else:
            grid[p[1]][p[0]] = 'o'


def sand_fall2(grid, p, a, s):
    if p[1]+1 > max_y:
        return None
    if grid[p[1]+1][p[0]] != '#' and grid[p[1]+1][p[0]] != 'o':
        return sand_fall2(grid, (p[0], p[1]+1), a, s)
    else:
        if grid[p[1]+1][p[0]-1] != '#' and grid[p[1]+1][p[0]-1] != 'o':
            return sand_fall2(grid, (p[0]-1, p[1]+1), a, s)
        elif grid[p[1]+1][p[0]+1] != '#' and grid[p[1]+1][p[0]+1] != 'o':
            return sand_fall2(grid, (p[0]+1, p[1]+1), a, s)
        else:
            grid[p[1]][p[0]] = 'o'
            if p == s:
                return a


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 14
    input = open("input.txt").read().splitlines()
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

    a = part1()
    print(f'{a = }')

    max_y += 2

    b = part2() + 1
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
