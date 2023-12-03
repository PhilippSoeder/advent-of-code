'''
Advent of Code 2023 - Day 3
'''
import aocd
from collections import defaultdict


def is_adjacent_to_symbol(number, r, c, m):
    s = c - len(number) + 1  # column start of number
    e = c  # column end of number
    result = False
    for r in [x for x in range(r-1, r+2) if x >= 0 and x < len(m)]:
        for c in [x for x in range(s-1, e+2) if x >= 0 and x < len(m[r])]:
            if not m[r][c].isdigit() and m[r][c] != ".":
                result = True
                # is gear? (part b)
                if m[r][c] == "*":
                    gears[(r, c)].append(number)
    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 3
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0
    gears = defaultdict(list)

    for r, row in enumerate(input):
        number = ""
        for c, column in enumerate(row):
            if row[c].isdigit():
                number += str(row[c])
                if c == len(row)-1 or not row[c+1].isdigit():
                    if is_adjacent_to_symbol(number, r, c, input):
                        part_a += int(number)
                    number = ""

    for g in gears:
        if len(gears[g]) == 2:
            part_b += int(gears[g][0]) * int(gears[g][1])

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
