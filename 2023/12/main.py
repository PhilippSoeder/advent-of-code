'''
Advent of Code 2023 - Day 12
'''
import aocd
from functools import cache


@cache
def solve(conditions, groups, tmp):
    if len(conditions) == 0:
        if len(groups) == 0:
            if tmp is None or tmp == 0:
                return 1
        return 0
    if conditions[0] == ".":
        if tmp is not None and tmp > 0:
            return 0
        return solve(conditions[1:], groups, None)
    if conditions[0] == "?":
        if tmp is not None and tmp > 0:
            return solve(conditions[1:], groups, tmp - 1)
        elif tmp is not None:
            return solve(conditions[1:], groups, None)
        else:
            option_1 = 0
            if len(groups) > 0:
                option_1 = solve(conditions[1:], groups[1:], groups[0] - 1)
            option_2 = solve(conditions[1:], groups, None)
            return option_1 + option_2
    if conditions[0] == "#":
        if tmp is not None:
            if tmp == 0:
                return 0
            return solve(conditions[1:], groups, tmp - 1)
        else:
            if len(groups) > 0:
                return solve(conditions[1:], groups[1:], groups[0] - 1)
            else:
                return 0


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 12
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    part_a = 0
    part_b = 0

    for row in input:
        conditions, groups = row.split(" ")
        groups = tuple(map(int, groups.split(",")))
        part_a += solve(conditions, groups, None)
        conditions = "?".join([conditions for _ in range(5)])
        groups *= 5
        part_b += solve(conditions, groups, None)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
