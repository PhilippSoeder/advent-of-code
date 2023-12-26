'''
Advent of Code 2021 - Day 6
'''
import aocd


def simulate_fish(n):
    counts = {}
    for i in range(9):
        counts[i] = 0
    for fish in fishs:
        counts[fish] += 1
    days = 0
    for _ in range(n):
        days += 1
        yesterday = [counts[x] for x in range(len(counts))]
        for i in range(8, 0, -1):
            counts[i-1] = yesterday[i]
        counts[6] += yesterday[0]
        counts[8] = yesterday[0]
    t = 0
    for i in counts:
        t += counts[i]
    return t


AOC_YEAR = 2021
AOC_DAY = 6
example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
input = open(example).read()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

fishs = [int(x) for x in input.split(',')]

part1 = simulate_fish(80)
part2 = simulate_fish(256)

print(f'{part1 = }')
print(f'{part2 = }')

aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
