'''
Advent of Code 2023 - Day 23
'''
import aocd
from collections import defaultdict


def is_in_grid_and_not_pound(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != "#"


def add_intersections_to_nodes():
    for r, row in enumerate(grid):
        for c, element in enumerate(row):
            if element == "#":
                continue
            directions_count = 0
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if is_in_grid_and_not_pound(r + dr, c + dc):
                    directions_count += 1
            if directions_count >= 3:
                nodes.append((r, c))


def get_graph(part):
    if part == "a":
        directions = {
            "^": [(-1, 0)],
            ">": [(0, 1)],
            "v": [(1, 0)],
            "<": [(0, -1)],
            ".": [(-1, 0), (0, 1), (1, 0), (0, -1)]
        }
    elif part == "b":
        directions = defaultdict(lambda: [(-1, 0), (0, 1), (1, 0), (0, -1)])
    graph = {node: {} for node in nodes}
    for nr, nc in nodes:
        stack = [(nr, nc, 0)]
        seen = {(nr, nc)}
        while len(stack) > 0:
            r, c, steps = stack.pop()
            if steps != 0 and (r, c) in nodes:
                graph[(nr, nc)][(r, c)] = steps
                continue
            for dr, dc in directions[grid[r][c]]:
                if is_in_grid_and_not_pound(r + dr, c + dc) \
                   and (r + dr, c + dc) not in seen:
                    stack.append((r + dr, c + dc, steps + 1))
                    seen.add((r + dr, c + dc))
    return graph


def get_longest_path(node):
    result = -99999999999999999
    if node == end:
        return 0
    seen.add(node)
    for next in graph[node]:
        if next not in seen:
            result = max(result, graph[node][next] + get_longest_path(next))
    seen.remove(node)
    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 23
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    grid = []
    for line in input:
        grid.append([x for x in line])

    for c, element in enumerate(grid[0]):
        if element == ".":
            start = (0, c)
    for c, element in enumerate(grid[-1]):
        if element == ".":
            end = (len(grid) - 1, c)

    nodes = []
    nodes.append(start)
    nodes.append(end)
    add_intersections_to_nodes()

    graph = get_graph("a")
    seen = set()
    part_a = get_longest_path(start)

    graph = get_graph("b")
    seen = set()
    part_b = get_longest_path(start)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
