'''
Advent of Code 2020 - Day 1
'''
import aocd


AOC_YEAR = 2020
AOC_DAY = 1
input = open("input.txt").read().splitlines()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
input = [int(n) for n in input]
part_a = 0
for number in input:
    if AOC_YEAR - number in input:
        part_a = number * (AOC_YEAR - number)

part_b = 0
for number in input:
    minor_goal = AOC_YEAR - number
    for second_number in input:
        if minor_goal - second_number in input:
            part_b = number * second_number * (minor_goal - second_number)

print(f'{part_a = }')
print(f'{part_b = }')
aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
