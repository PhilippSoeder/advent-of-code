'''
Advent of Code 2023 - Day 1
'''
import aocd


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 1
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    words = "one two three four five six seven eight nine".split(" ")

    part_a = 0
    part_b = 0

    for line in input:
        digits_in_line = [x for x in line if x.isdigit()]
        part_a += int(str(digits_in_line[0]) + str(digits_in_line[-1]))
        for cnt, nbr in enumerate(words):
            line = line.replace(nbr, nbr + str(cnt+1) + nbr)
        digits_in_line = [x for x in line if x.isdigit()]
        part_b += int(str(digits_in_line[0]) + str(digits_in_line[-1]))

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
