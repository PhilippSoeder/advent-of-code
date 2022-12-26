'''
Advent of Code 2022 - Day 10
'''
import aocd


def determine_signal(c, r):
    if (c % 40) == 20:
        return c * r
    else:
        return 0


def change_crt(c, r):
    sprite = create_sprite(r)
    column = (c - 1) % 40
    row = int((c - 1) / 40)
    if sprite[column] == '#':
        crt[row][column] = '#'


def create_sprite(r):
    sprite = ['.' for _ in range(40)]
    if r > 0:
        sprite[r-1] = '#'
    sprite[r] = '#'
    if r < 39:
        sprite[r+1] = '#'
    return sprite


def print_crt(crt):
    for row in crt:
        for column in row:
            print(column, end='')
        print()


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 10
    # input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    instructions = []
    for line in input:
        x = line.split()
        if len(x) > 1:
            x = [x[0], int(x[1])]
        instructions.append(x)

    crt = []
    for _ in range(6):
        r1 = []
        for _ in range(40):
            r1.append('.')
        crt.append(r1)

    c = 0
    r = 1
    a = 0
    for line in instructions:
        c += 1
        match line[0]:
            case 'noop':
                a += determine_signal(c, r)
                change_crt(c, r)
            case 'addx':
                a += determine_signal(c, r)
                change_crt(c, r)
                c += 1
                a += determine_signal(c, r)
                change_crt(c, r)
                r += line[1]

    print(f'{a = }')

    print('b: ')
    print_crt(crt)

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    # aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
