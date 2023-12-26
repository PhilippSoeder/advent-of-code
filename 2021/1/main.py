'''
Advent of Code 2021 - Day 1
'''
import aocd


def part_1(input):
    result = 0
    last = None
    for line in input:
        if last is not None:
            if last < line:
                result += 1
        last = line
    return result


def part_2(input):
    result = 0
    last = None
    for i in range(0, len(input)-1):
        if i+2 > len(input)-1:
            break
        a = input[i]
        b = input[i+1]
        c = input[i+2]
        current = a + b + c
        if last is not None:
            if last < current:
                result += 1
        last = current
    return result


AOC_YEAR = 2021
AOC_DAY = 1
example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
input = open(example).read().splitlines()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
input = list(map(int, input))

part1 = part_1(input)
part2 = part_2(input)

print(f'{part1 = }')
print(f'{part2 = }')

aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
