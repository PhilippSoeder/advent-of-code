'''
Advent of Code 2022 - Day 22
'''
import aocd
import re


def init_from_input():
    input_b, i = input.split('\n\n')
    input_b = input_b.splitlines()
    b = []
    p = [-1, -1]
    d = 0
    m = (0, 1)

    for line in input_b:
        b.append(list(line))

    max_c = 0
    for r in b:
        max_c = max(max_c, len(r))

    for r, row in enumerate(b):
        missing_c = max_c - len(row)
        for _ in range(missing_c):
            b[r].append(' ')

    for r, row in enumerate(b):
        for c, _ in enumerate(b):
            if b[r][c] == '.':
                p = [r, c]
                break

        if p != [-1, -1]:
            break

    i = re.findall(r'[RL]|\d+', i)

    return b, p, i, d, m


def solve(part):
    b, p, i, d, m = init_from_input()

    for instr in i:
        if instr.isdigit():
            for _ in range(int(instr)):
                if part == 'a':
                    pn = [(p[0]+m[0]) % len(b), (p[1]+m[1]) % len(b[0])]

                    while b[pn[0]][pn[1]] == ' ' and b[pn[0]][pn[1]] != '#':
                        pn = [(pn[0]+m[0]) % len(b), (pn[1]+m[1]) % len(b[0])]

                    if b[pn[0]][pn[1]] == '#':
                        break

                    p = pn
                elif part == 'b':
                    m_before = m
                    pn = [p[0]+m[0], p[1]+m[1]]

                    if pn[0] < 0 and 100 <= pn[1] < 150 and m == (-1, 0):
                        pn = [199, pn[1]-100]
                    elif pn[0] >= 200 and 0 <= pn[1] < 50 and m == (1, 0):
                        pn = [0, pn[1]+100]
                    elif pn[0] < 0 and 50 <= pn[1] < 100 and m == (-1, 0):
                        m = (0, 1)
                        pn = [pn[1]+100, 0]
                    elif 0 <= pn[0] < 50 and pn[1] == 49 and m == (0, -1):
                        m = (0, 1)
                        pn = [149-pn[0], 0]
                    elif 100 <= pn[0] < 150 and pn[1] < 0 and m == (0, -1):
                        m = (0, 1)
                        pn = [149-pn[0], 50]
                    elif pn[0] == 99 and 0 <= pn[1] < 50 and m == (-1, 0):
                        m = (0, 1)
                        pn = [pn[1]+50, 50]
                    elif 0 <= pn[0] < 50 and pn[1] >= 150 and m == (0, 1):
                        m = (0, -1)
                        pn = [149-pn[0], 99]
                    elif pn[0] == 50 and 100 <= pn[1] < 150 and m == (1, 0):
                        m = (0, -1)
                        pn = [pn[1]-50, 99]
                    elif pn[0] == 150 and 50 <= pn[1] < 100 and m == (1, 0):
                        m = (0, -1)
                        pn = [pn[1]+100, 49]
                    elif 100 <= pn[0] < 150 and pn[1] == 100 and m == (0, 1):
                        m = (0, -1)
                        pn = [149-pn[0], 149]
                    elif 150 <= pn[0] < 200 and pn[1] < 0 and m == (0, -1):
                        m = (1, 0)
                        pn = [0, pn[0]-100]
                    elif 50 <= pn[0] < 100 and pn[1] == 49 and m == (0, -1):
                        m = (1, 0)
                        pn = [100, pn[0]-50]
                    elif 150 <= pn[0] < 200 and pn[1] == 50 and m == (0, 1):
                        m = (-1, 0)
                        pn = [149, pn[0]-100]
                    elif 50 <= pn[0] < 100 and pn[1] == 100 and m == (0, 1):
                        m = (-1, 0)
                        pn = [49, pn[0]+50]

                    if b[pn[0]][pn[1]] == '#':
                        m = m_before
                        break

                    if m == (0, 1):
                        d = 0
                    elif m == (1, 0):
                        d = 1
                    elif m == (0, -1):
                        d = 2
                    elif m == (-1, 0):
                        d = 3

                    p = pn
        else:
            if instr == 'R':
                d = (d + 1) % 4
            elif instr == 'L':
                d = (d - 1) % 4

            match d:
                case 0:
                    m = (0, 1)
                case 1:
                    m = (1, 0)
                case 2:
                    m = (0, -1)
                case 3:
                    m = (-1, 0)

    return (1000 * (p[0]+1)) + (4 * (p[1]+1)) + d


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 22
    input = open("input.txt").read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

    part1 = solve(part='a')
    part2 = solve(part='b')

    print(f'{part1 = }')
    print(f'{part2 = }')

    aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
