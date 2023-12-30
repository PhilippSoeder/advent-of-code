'''
Advent of Code 2022 - Day 17
'''
import aocd
import copy


def get_highest_stopped(chamber):
    highest_stopped = [len(chamber) for _ in range(CHAMBER_WIDTH)]
    for c in range(CHAMBER_WIDTH):
        for r, _ in enumerate(chamber):
            if chamber[r][c] == '#':
                highest_stopped[c] = r
                break
    return tuple(highest_stopped)


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 17
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
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
    states_seen = {}
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
        i += 1
        state = (rocks, iterator_pushes, get_highest_stopped(chamber))
        if state in states_seen:
            si, slc = states_seen[state]
            k = NUMBER_OF_ROCKS_TO_STOP_2 - i
            q = k // (i - si)
            o = q * (len(chamber) - slc)
            i += q * (i - si)
            states_seen = {}
        states_seen[state] = (i, len(chamber))
        if i == NUMBER_OF_ROCKS_TO_STOP_1:
            a = len(chamber)
            print(f'{a = }')
        if i == NUMBER_OF_ROCKS_TO_STOP_2:
            b = len(chamber) + o
            print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
