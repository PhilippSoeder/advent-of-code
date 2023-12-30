'''
Advent of Code 2022 - Day 25
'''
import aocd


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 25
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    part1 = ""
    dec = 0
    for line in input:
        a = 1
        nbr = [x for x in line[::-1]]
        for c, char in enumerate(nbr):
            nbr[c] = nbr[c].replace('-', '-1')
            nbr[c] = nbr[c].replace('=', '-2')
            dec += int(nbr[c]) * a
            a *= 5

    while dec > 0:
        r = dec % 5
        dec = dec // 5
        if r <= 2:
            part1 = str(r) + part1
        else:
            part1 = ['=', '-'][r-3] + part1
            dec += 1

    print(f'{part1 = }')
    aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
