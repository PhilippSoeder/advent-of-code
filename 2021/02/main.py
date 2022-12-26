'''
Advent of Code 2021 - Day 2
'''
import aocd


def part_1():
    horizontal = 0
    depth = 0
    for line in input:
        direction, amount = line.split()
        match direction:
            case 'forward':
                horizontal += int(amount)
            case 'up':
                depth -= int(amount)
            case 'down':
                depth += int(amount)
    return horizontal * depth


def part_2():
    horizontal = 0
    depth = 0
    aim = 0
    for line in input:
        direction, amount = line.split()
        match direction:
            case 'forward':
                horizontal += int(amount)
                depth += aim * int(amount)
            case 'up':
                aim -= int(amount)
            case 'down':
                aim += int(amount)
    return horizontal * depth


AOC_YEAR = 2021
AOC_DAY = 2
input = open("input.txt").read().splitlines()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

part1 = part_1()
part2 = part_2()

print(f'{part1 = }')
print(f'{part2 = }')

aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
