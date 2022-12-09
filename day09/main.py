'''
Advent of Code 2022 - Day 9
'''
import aocd
import math


def run(n: int) -> int:
    visited = {}
    k = [(0, 0) for _ in range(n+1)]
    visited[k[len(k)-1]] = True
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
                k[j] = move_tail(k[j-1], k[j])
            visited[k[len(k)-1]] = True
    return len(visited)


def move_tail(H, T):
    if abs(H[0]-T[0]) > 1 or abs(H[1]-T[1]) > 1:
        d = (H[0]-T[0], H[1]-T[1])
        if d[0] == 0:
            T = (T[0], int(T[1]+sign(d[1])))
        elif d[1] == 0:
            T = (int(T[0]+sign(d[0])), T[1])
        else:
            T = (int(T[0]+sign(d[0])), int(T[1]+sign(d[1])))
    return T


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
