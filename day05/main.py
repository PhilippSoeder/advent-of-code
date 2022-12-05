'''
Advent of Code 2022 - Day 5
'''
import aocd
import re


def part1() -> int:
    for instruction in instructions:
        amount, from_index, to_index = re.findall(r'[0-9]+', instruction)
        for _ in range(int(amount)):
            c = crates[int(from_index)-1].pop()
            crates[int(to_index)-1].append(c)
    result = []
    for stack in crates:
        p = stack.pop()
        result.append(p)
    result = "".join([str(i) for i in result])
    return result


def part2() -> int:
    for instruction in instructions:
        amount, from_index, to_index = re.findall(r'[0-9]+', instruction)
        tmp = []
        for _ in range(int(amount)):
            c = crates[int(from_index)-1].pop()
            tmp.append(c)
        crates[int(to_index)-1].extend(list(reversed(tmp)))
    result = []
    for stack in crates:
        p = stack.pop()
        result.append(p)
    result = "".join([str(i) for i in result])
    return result


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 5
    input = open("input.txt").read().splitlines()

    crates = [
        ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
        ['M', 'Q', 'H'],
        ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
        ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
        ['M', 'T', 'H', 'P'],
        ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
        ['M', 'N', 'B', 'F', 'V', 'R'],
        ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
        ['P', 'D', 'B', 'C', 'N']
    ]

    instructions = []
    for i, line in enumerate(input):
        if i > 9:
            instructions.append(line)

    a = part1()
    print(f'{a = }')

    crates = [
        ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
        ['M', 'Q', 'H'],
        ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
        ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
        ['M', 'T', 'H', 'P'],
        ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
        ['M', 'N', 'B', 'F', 'V', 'R'],
        ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
        ['P', 'D', 'B', 'C', 'N']
    ]

    b = part2()
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
