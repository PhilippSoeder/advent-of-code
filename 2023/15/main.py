'''
Advent of Code 2023 - Day 15
'''
import aocd
import re
from collections import defaultdict


def solve_a(init_seq):
    result = 0
    for i in init_seq:
        result += hash_seq(i)
    return result


def solve_b(init_seq):
    result = 0
    boxes = defaultdict(list)
    for seq in init_seq:
        label, value = re.split(r"=|-", seq)
        box = hash_seq(label)
        if "=" in seq:
            for b, bx in enumerate(boxes[box]):
                if label in bx:
                    boxes[box][b] = (label, int(value))
                    break
            else:
                boxes[box].append((label, int(value)))
        elif "-" in seq:
            for b in boxes[box]:
                if label in b:
                    boxes[box].remove(b)
    for box in boxes:
        focusing_power = 0
        for index, lens in enumerate(boxes[box]):
            focusing_power += (box + 1) * (index + 1) * lens[1]
        result += focusing_power
    return result


def hash_seq(seq):
    global seen
    if seq in seen:
        return seen[seq]
    else:
        result = 0
        for char in seq:
            result += ord(char)
            result *= 17
            result %= 256
        seen[seq] = result
        return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 15
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

    init_seq = input.split(",")

    seen = {}

    part_a = solve_a(init_seq)
    part_b = solve_b(init_seq)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
