'''
Advent of Code 2023 - Day 11
'''
import aocd
from itertools import combinations


def explore_free(map):
    horizontal_free = []
    vertical_free = []
    for r, _ in enumerate(map):
        if "#" not in map[r]:
            horizontal_free.append(r)
        column = [x[r] for x in map]
        if "#" not in column:
            vertical_free.append(r)
    return horizontal_free, vertical_free


def get_galaxies(map, rf, cf, e):
    galaxies = []
    for r, row in enumerate(map):
        for c, _ in enumerate(row):
            if map[r][c] == "#":
                rfc = len([x for x in rf if x < r])
                cfc = len([x for x in cf if x < c])
                galaxies.append((r + rfc * (e-1), c + cfc * (e-1)))
    return galaxies


def distance(galaxy1, galaxy2):
    x1, y1 = galaxy1
    x2, y2 = galaxy2
    return abs(x1 - x2) + abs(y1 - y2)


def total_distance(galaxies):
    total_distance = 0
    all_pairs = combinations(galaxies, 2)
    for pair in all_pairs:
        total_distance += distance(pair[0], pair[1])
    return total_distance


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 11
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    map = []
    for line in input:
        map.append([x for x in line])

    horizontal_free, vertical_free = explore_free(map)

    galaxies = get_galaxies(map, horizontal_free, vertical_free, 2)
    part_a = total_distance(galaxies)

    galaxies = get_galaxies(map, horizontal_free, vertical_free, 1000000)
    part_b = total_distance(galaxies)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
