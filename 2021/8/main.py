'''
Advent of Code 2021 - Day 8
'''
import aocd


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 8
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0

    mapping = [None for _ in range(10)]

    for line in input:
        usp, output_values = line.split("|")
        usp = usp.split()
        output_values = output_values.split()
        for n in output_values:
            if len(n) in (2, 3, 4, 7):
                part_a += 1
        usp.sort(key=lambda x: len(x))
        usp = usp[:3] + usp[6:] + usp[3:6]
        for i in usp:
            if len(i) == 2:
                mapping[1] = sorted(i)
            elif len(i) == 3:
                mapping[7] = sorted(i)
            elif len(i) == 4:
                mapping[4] = sorted(i)
            elif len(i) == 5:
                if set(mapping[1]).issubset(set(i)):
                    mapping[3] = sorted(i)
                elif set(i).issubset(set(mapping[9])):
                    mapping[5] = sorted(i)
                else:
                    mapping[2] = sorted(i)
            elif len(i) == 6:
                if not set(mapping[1]).issubset(set(i)):
                    mapping[6] = sorted(i)
                elif set(mapping[4]).issubset(set(i)):
                    mapping[9] = sorted(i)
                else:
                    mapping[0] = sorted(i)
            elif len(i) == 7:
                mapping[8] = sorted(i)
        number = ""
        for n in output_values:
            number += str(mapping.index(sorted(n)))
        part_b += int(number)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
