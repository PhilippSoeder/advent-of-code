'''
Advent of Code 2023 - Day 8
'''
import aocd
from math import gcd


def solve(instructions, nodes, locations):
    destination_reached = False
    reached = {}
    steps = 0
    while not destination_reached:
        for d in instructions:
            for l, location in enumerate(locations):
                locations[l] = nodes[location][d]
            steps += 1
        for node in locations:
            if node[-1] == "Z" and reached.get(node) is None:
                reached[node] = steps
        if len(reached) == len(locations):
            a = []
            for i, item in enumerate(reached):
                a.append(reached[item])
            result = 1
            for i in a:
                result = result * i // gcd(result, i)
            break
    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 8
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    #instructions, rest = open(example).read().split("\n\n")
    instruct, rest = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).split("\n\n")
    rest = rest.split("\n")
    nodes = {}
    for node in rest:
        s, d = node.split(" = ")
        d1, d2 = d.split(', ')
        nodes[s] = {"L": d1[1:], "R": d2[:-1]}

    part_a = 0
    part_b = 0

    # part a
    locations = ["AAA"]
    part_a = solve(instruct, nodes, locations)

    # part b
    locations = []
    for node in nodes:
        if node[-1] == "A":
            locations.append(node)
    part_b = solve(instruct, nodes, locations)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
