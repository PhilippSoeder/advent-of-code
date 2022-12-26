'''
Advent of Code 2021 - Day 5
'''
import aocd
import math


def sign(x):
    return math.copysign(1, x)


def run(part):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for line in input:
        a, b, c, d = line.split(',')
        x1.append(int(a))
        y1.append(int(b))
        x2.append(int(c))
        y2.append(int(d))

    max_x = max(max(x1), max(x2))
    max_y = max(max(y1), max(y2))

    board = []
    for _ in range(0, max_x+1):
        tmp = []
        for _ in range(0, max_y+1):
            tmp.append(0)
        board.append(tmp)

    for line in input:
        x1, y1, x2, y2 = line.split(',')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 == x2:
            y1_n = min(y1, y2)
            y2_n = max(y1, y2)
            for i in range(y1_n, y2_n+1):
                board[i][x1] += 1
        elif y1 == y2:
            x1_n = min(x1, x2)
            x2_n = max(x1, x2)
            for i in range(x1_n, x2_n+1):
                board[y1][i] += 1
        else:
            if part == 'b':
                dx = x2 - x1
                dy = y2 - y1
                for i in range(abs(dx)+1):
                    board[y1 + int(sign(dy) * i)][x1 + int(sign(dx) * i)] += 1

    cnt = 0
    for line in board:
        for element in line:
            if element >= 2:
                cnt += 1
    return cnt


AOC_YEAR = 2021
AOC_DAY = 5
input = open("input.txt").read().replace(' -> ', ',').splitlines()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).replace(' -> ', ',').splitlines()

part1 = run(part='a')
print(f'{part1 = }')

part2 = run(part='b')
print(f'{part2 = }')

aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
