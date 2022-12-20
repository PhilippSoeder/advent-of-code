'''
Advent of Code 2022 - Day 17
'''
import aocd
import copy


def print_chamber():
    for line in chamber:
        print('|', end=' ')
        for char in line:
            print(char, end=' ')
        print('|')


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 17
    input = open("input.txt").read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)
    direction_push = [x for x in input]

    CHAMBER_WIDTH = 7
    NUMBER_OF_ROCKS_TO_STOP_1 = 2022
    NUMBER_OF_ROCKS_TO_STOP_2 = 1000000000000

    rock_types = [
                    [
                        ['.', '.', '@', '@', '@', '@', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.']
                    ],
                    [
                        ['.', '.', '.', '@', '.', '.', '.'],
                        ['.', '.', '@', '@', '@', '.', '.'],
                        ['.', '.', '.', '@', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.']
                    ],
                    [
                        ['.', '.', '.', '.', '@', '.', '.'],
                        ['.', '.', '.', '.', '@', '.', '.'],
                        ['.', '.', '@', '@', '@', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.']
                    ],
                    [
                        ['.', '.', '@', '.', '.', '.', '.'],
                        ['.', '.', '@', '.', '.', '.', '.'],
                        ['.', '.', '@', '.', '.', '.', '.'],
                        ['.', '.', '@', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.']
                    ],
                    [
                        ['.', '.', '@', '@', '.', '.', '.'],
                        ['.', '.', '@', '@', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.']
                    ]
                ]

    a = 0
    b = 0
    i = 0
    chamber = []
    rocks = 0
    iterator_pushes = 0
    result = 0
    while i <= NUMBER_OF_ROCKS_TO_STOP_2:
        offset = 0
        height_new_rock = len(rock_types[rocks]) - 3
        new_rock = copy.deepcopy(rock_types[rocks])
        chamber = new_rock + chamber
        rocks = (rocks + 1) % len(rock_types)

        falling_stoped = False
        while not falling_stoped:
            space = True
            match direction_push[iterator_pushes]:
                case '<':
                    for r in range(offset, height_new_rock+offset):
                        if chamber[r][0] == '@':
                            space = False
                            break
                        for c in range(1, CHAMBER_WIDTH):
                            if chamber[r][c] == '@' and chamber[r][c-1] == '#':
                                space = False
                                break
                    if space:
                        for r in range(offset, height_new_rock+offset):
                            for c in range(1, CHAMBER_WIDTH):
                                if chamber[r][c] == '@':
                                    chamber[r][c-1] = '@'
                                    chamber[r][c] = '.'
                case '>':
                    for r in range(offset, height_new_rock+offset):
                        if chamber[r][CHAMBER_WIDTH-1] == '@':
                            space = False
                            break
                        for c in range(CHAMBER_WIDTH-2, -1, -1):
                            if chamber[r][c] == '@' and chamber[r][c+1] == '#':
                                space = False
                                break
                    if space:
                        for r in range(offset, height_new_rock+offset):
                            for c in range(CHAMBER_WIDTH-2, -1, -1):
                                if chamber[r][c] == '@':
                                    chamber[r][c+1] = '@'
                                    chamber[r][c] = '.'
            iterator_pushes = (iterator_pushes + 1) % len(direction_push)

            if height_new_rock+offset == len(chamber):
                falling_stoped = True
            else:
                for r in range(height_new_rock-1+offset, -1, -1):
                    for c in range(CHAMBER_WIDTH):
                        if chamber[r][c] == '@' and chamber[r+1][c] == '#':
                            falling_stoped = True
                            break
            if falling_stoped:
                for r in range(offset, height_new_rock+offset):
                    for c in range(CHAMBER_WIDTH):
                        if chamber[r][c] == '@':
                            chamber[r][c] = '#'
            else:
                for r in range(height_new_rock+offset-1, -1, -1):
                    for c in range(CHAMBER_WIDTH):
                        if chamber[r][c] == '@':
                            chamber[r][c] = '.'
                            chamber[r+1][c] = '@'
                if chamber[0] == ['.', '.', '.', '.', '.', '.', '.']:
                    del chamber[0]
                else:
                    offset += 1
        if i == NUMBER_OF_ROCKS_TO_STOP_1-1:
            a = len(chamber)
            print(f'{a = }')
        if i == NUMBER_OF_ROCKS_TO_STOP_2-1:
            b = len(chamber)
            print(f'{b = }')
        i += 1

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
