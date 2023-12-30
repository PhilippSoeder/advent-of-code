'''
Advent of Code 2022 - Day 6
'''
import aocd


def get_start_of_message(start_bits: int) -> int:
    som = ['' for _ in range(start_bits)]
    for index, char in enumerate(input):
        som[index % start_bits] = char
        if index >= start_bits-1:
            if len(set(som)) == start_bits:
                return index + 1


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 6
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

    a = get_start_of_message(4)
    b = get_start_of_message(14)

    print(f'{a = }')
    print(f'{b = }')

    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
