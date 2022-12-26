'''
Advent of Code 2022 - Day 8
'''
import aocd


def is_visible(r: int, c: int) -> bool:
    top, bottom, left, right = True, True, True, True
    for row in range(r, 0, -1):
        if f[r][c] <= f[row-1][c]:
            top = False
    for row in range(r, len(f)-1):
        if f[r][c] <= f[row+1][c]:
            bottom = False
    for column in range(c, 0, -1):
        if f[r][c] <= f[r][column - 1]:
            left = False
    for column in range(c, len(f[r])-1):
        if f[r][c] <= f[r][column + 1]:
            right = False
    return top or bottom or left or right


def part1() -> int:
    t = 0
    for r, row in enumerate(f):
        for c, column in enumerate(row):
            if r == 0 or c == 0 or r == len(f)-1 or c == len(f[r])-1:
                t += 1
            else:
                if is_visible(r, c):
                    t += 1
    return t


def part2() -> int:
    t = 0
    for r, row in enumerate(f):
        for c, t_height in enumerate(row):
            top, bottom, left, right = 0, 0, 0, 0
            for i in range(r, 0, -1):
                top += 1
                if f[r][c] <= f[i-1][c]:
                    break
            for i in range(r, len(f)-1):
                bottom += 1
                if f[r][c] <= f[i+1][c]:
                    break
            for j in range(c, 0, -1):
                left += 1
                if f[r][c] <= f[r][j - 1]:
                    break
            for j in range(c, len(f[r])-1):
                right += 1
                if f[r][c] <= f[r][j + 1]:
                    break
            scenic_score = top * bottom * left * right
            if scenic_score > t:
                t = scenic_score
    return t


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 8
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    f = []
    for r, line in enumerate(input):
        f.append([])
        for c, column in enumerate(line):
            f[r].append(column)

    a = part1()
    print(f'{a = }')

    b = part2()
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
