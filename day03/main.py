'''
Advent of Code 2022 - Day 3
'''


def get_items() -> list:
    with open("input.txt") as input:
        return input.read().splitlines()


def get_itm_value(result):
    if result[0].isupper():
        return ord(result[0]) - 38
    else:
        return ord(result[0]) - 96


def part1() -> int:
    halfs = []
    for bag in bags:
        half = int(len(bag)/2)
        first_half = bag[:half]
        second_half = bag[half:]
        halfs.append([first_half, second_half])
    sum = 0
    for half in halfs:
        overlap = [x for x in list(half[0]) if x in list(half[1])]
        sum += get_itm_value(overlap)
    return sum


def part2() -> int:
    counter = 0
    groups = []
    for bag in bags:
        if counter % 3 == 0:
            groups.append([bag])
        else:
            groups[-1].append(bag)
        counter += 1
    sum = 0
    for group in groups:
        common = ''.join(set.intersection(*map(set, group)))
        sum += get_itm_value(common)
    return sum


if __name__ == '__main__':
    bags = get_items()

    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
