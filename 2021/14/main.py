'''
Advent of Code 2021 - Day 14
'''
import aocd
from collections import Counter


def get_score(counter):
    max_v = max(counter.values())
    min_v = min(counter.values())
    return max_v - min_v


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 14
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)
    polymer_template, pi_rules = input.split("\n\n")
    rules = {}
    for line in pi_rules.splitlines():
        key, value = line.split(" -> ")
        rules[key] = value

    pair_count = Counter()
    for i in range(len(polymer_template) - 1):
        pair_count[polymer_template[i:i+2]] += 1

    step = 0
    while True:
        step += 1
        new_count = Counter()
        char_count = Counter()
        for key, value in pair_count.items():
            new_count[f"{key[0]}{rules[key]}"] += value
            new_count[f"{rules[key]}{key[1]}"] += value
            char_count[key[0]] += value
            char_count[rules[key]] += value
        char_count[polymer_template[-1]] += 1
        pair_count = new_count

        if step == 10:
            part_a = get_score(char_count)
        if step == 40:
            part_b = get_score(char_count)
            break

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
