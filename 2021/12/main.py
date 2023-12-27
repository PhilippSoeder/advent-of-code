'''
Advent of Code 2021 - Day 12
'''
import aocd
from collections import defaultdict


def solve(nodes, part):
    paths = []
    q = [(["start"], {"start"}, None)]
    while len(q) > 0:
        (path, seen, seen_twice) = q.pop(0)
        if path[-1] == "end":
            paths.append(path)
            continue
        for n in nodes[path[-1]]:
            if n.islower():
                if n not in seen:
                    q.append((path + [n], seen | {n}, seen_twice))
                elif part == "b":
                    if n != "start" and seen_twice is None:
                        q.append((path + [n], seen, n))
            elif n.isupper():
                q.append((path + [n], seen, seen_twice))
    return len(paths)


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 12
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0

    nodes = defaultdict(lambda: [])
    for line in input:
        n1, n2 = line.split("-")
        nodes[n1].append(n2)
        nodes[n2].append(n1)

    part_a = solve(nodes, "a")
    part_b = solve(nodes, "b")

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
