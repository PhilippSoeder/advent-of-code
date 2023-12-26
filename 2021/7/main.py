'''
Advent of Code 2021 - Day 7
'''
import aocd
import sys


AOC_YEAR = 2021
AOC_DAY = 7
example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
input = open(example).read()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

submarines = list(map(int, input.split(',')))
min_s = min(submarines)
max_s = max(submarines)
part1 = sys.maxsize
part2 = sys.maxsize
for i in range(min_s, max_s+1):
    a = 0
    b = 0
    for s in submarines:
        abs_diff = abs(s-i)
        a += abs_diff
        b += int((abs_diff * (abs_diff + 1)) / 2)
    part1 = min(part1, a)
    part2 = min(part2, b)
print(f'{part1 = }')
print(f'{part2 = }')
aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
