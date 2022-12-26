'''
Advent of Code 2021 - Day 3
'''
import aocd


def get_gamma_and_epsilon_rate(n):
    gr = ''
    er = ''
    for i, _ in enumerate(n[0]):
        a = [x[i] for x in n]
        ones = [x for x in a if x == '1']
        zeros = [x for x in a if x == '0']
        if len(ones) > len(zeros):
            gr += '1'
            er += '0'
        else:
            gr += '0'
            er += '1'
    return int(gr), int(er)


def get_oxygen_generator_rating(n):
    i = 0
    while len(n) > 1:
        a = [x[i] for x in n]
        zeros_a = len([x for x in a if x == '0'])
        ones_a = len([x for x in a if x == '1'])
        if ones_a >= zeros_a:
            n = [x for x in n if x[i] == '1']
        else:
            n = [x for x in n if x[i] == '0']
        i += 1
    return int(''.join(n[0]))


def get_CO2_scrubber_rating(n):
    i = 0
    while len(n) > 1:
        b = [x[i] for x in n]
        zeros_b = len([x for x in b if x == '0'])
        ones_b = len([x for x in b if x == '1'])
        if ones_b >= zeros_b:
            n = [x for x in n if x[i] == '0']
        else:
            n = [x for x in n if x[i] == '1']
        i += 1
    return int(''.join(n[0]))


def binary_to_decimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


AOC_YEAR = 2021
AOC_DAY = 3
input = open("input.txt").read().splitlines()
input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
numbers = []
for line in input:
    numbers.append(list(line))

gr, er = get_gamma_and_epsilon_rate(numbers)
part1 = binary_to_decimal(gr) * binary_to_decimal(er)
print(f'{part1 = }')
aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)

ogr = get_oxygen_generator_rating(numbers)
CO2sr = get_CO2_scrubber_rating(numbers)
part2 = binary_to_decimal(ogr) * binary_to_decimal(CO2sr)
print(f'{part2 = }')
aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
