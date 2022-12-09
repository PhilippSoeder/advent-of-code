'''
Advent of Code 2022 - Day 9
'''
import aocd
import math


def run(n: int) -> int:
    v = {}
    k = [(0, 0) for _ in range(n+1)]
    v[k[len(k)-1]] = True
    for i in instructions:
        for _ in range(i[1]):
            match i[0]:
                case 'U':
                    k[0] = (k[0][0], k[0][1]+1)
                case 'D':
                    k[0] = (k[0][0], k[0][1]-1)
                case 'R':
                    k[0] = (k[0][0]+1, k[0][1])
                case 'L':
                    k[0] = (k[0][0]-1, k[0][1])
            for j in range(1, len(k)):
                k[j] = move_knot(k[j-1], k[j])
            v[k[len(k)-1]] = True
    return len(v)


def move_knot(k1, k2):
    if abs(k1[0]-k2[0]) > 1 or abs(k1[1]-k2[1]) > 1:
        d = (k1[0]-k2[0], k1[1]-k2[1])
        if d[0] == 0:
            k2 = (k2[0], int(k2[1]+sign(d[1])))
        elif d[1] == 0:
            k2 = (int(k2[0]+sign(d[0])), k2[1])
        else:
            k2 = (int(k2[0]+sign(d[0])), int(k2[1]+sign(d[1])))
    return k2


def sign(x):
    return math.copysign(1, x)


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 9
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    instructions = []
    for line in input:
        direction, amount = line.split()
        instructions.append([direction, int(amount)])

    a = run(1)
    print(f'{a = }')

    b = run(9)
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
