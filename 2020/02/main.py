'''
Advent of Code 2020 - Day 2
'''
import aocd


AOC_YEAR = 2020
AOC_DAY = 2
input = open("input.txt").read().splitlines()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
part_a = 0
part_b = 0

for line in input:
    range, letter, password = line.split(" ")
    range_a, range_b = range.split("-")
    range_a = int(range_a)
    range_b = int(range_b)
    letter = letter[:-1]

    # part a
    occourances = password.count(letter)
    if min(range_a, range_b) <= occourances <= max(range_a, range_b):
        part_a += 1

    # part b
    if password[range_a-1] == letter and password[range_b-1] != letter or \
       password[range_a-1] != letter and password[range_b-1] == letter:
        part_b += 1

print(f'{part_a = }')
print(f'{part_b = }')
aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
