'''
Advent of Code 2023 - Day 25
'''
import aocd
from collections import defaultdict
import networkx


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 25
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = None

    components = defaultdict(set)
    for line in input:
        component, connected_components = line.split(": ")
        connected_components = connected_components.split()
        for connected in connected_components:
            components[component].add(connected)
            components[connected].add(component)

    graph = networkx.Graph()
    for component in components:
        for connected in components[component]:
            graph.add_edge(component, connected, capacity=1)

    for s in components:
        for t in components:
            if s == t:
                continue
            cut_value, (set_1, set_2) = networkx.minimum_cut(graph, s, t)
            if cut_value == 3:
                part_a = len(set_1) * len(set_2)
                break
        if part_a is not None:
            break

    print(f"{part_a = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
