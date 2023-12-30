'''
Advent of Code 2022 - Day 13
'''
import aocd


def part1(input):
    pairs = []
    input = input.split("\n\n")
    for pair in input:
        left, right = pair.splitlines()
        pairs.append((eval(left), eval(right)))
    a = 0
    for i, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) < 0:
            a += i + 1
    return a


def part2(input):
    input = input.splitlines()
    input = [eval(x) for x in input if x != '']
    sep_1 = [[2]]
    input.append(sep_1)
    sep_2 = [[6]]
    input.append(sep_2)
    n = len(input)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if compare(input[j], input[j + 1]) > 0:
                swapped = True
                input[j], input[j + 1] = input[j + 1], input[j]
        if not swapped:
            return
    r = 1
    for i, item in enumerate(input):
        if item == sep_1 or item == sep_2:
            r *= i+1
    return r


def compare(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == list and type(right) == list:
        for left_zip, right_zip in zip(left, right):
            tmp = compare(left_zip, right_zip)
            if tmp != 0:
                return tmp
        return len(left) - len(right)


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 13

    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

    a = part1(input)
    b = part2(input)

    print(f'{a = }')
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
