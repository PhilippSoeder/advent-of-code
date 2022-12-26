'''
Advent of Code 2022 - Day 24
'''
import aocd
from collections import deque


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 24
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    part1 = 0
    part2 = 0

    grid = []
    for r, line in enumerate(input[1:-1]):
        row = []
        for c, item in enumerate(line[1:-1]):
            row.append(item)
        grid.append(row)

    start = (-1, 0)
    end = (len(grid), len(grid[0])-1)
    p = start

    directions = {
                    '0': (0, 0),
                    '>': (0, 1),
                    'v': (1, 0),
                    '<': (0, -1),
                    '^': (-1, 0)
                }

    blizzards = []
    for r, row in enumerate(grid):
        for c, column in enumerate(row):
            if grid[r][c] in directions:
                blizzards.append((r, c, grid[r][c]))

    seen_states = set()
    state = (p, tuple(blizzards))
    queue = deque()
    queue.append((state, 0))
    rnd = 0
    while len(queue) > 0:
        item = queue.popleft()
        state, i = item
        p, blizzards = state

        if p == end:
            if rnd == 0:
                part1 = i
                print(f'{part1 = }')
                start, end = end, start
                state = (p, tuple(blizzards))
                queue = deque()
                seen_states = set()
                queue.append((state, i))
                rnd += 1
                continue
            elif rnd == 1:
                start, end = end, start
                state = (p, tuple(blizzards))
                queue = deque()
                seen_states = set()
                queue.append((state, i))
                rnd += 1
                continue
            else:
                part2 = i
                print(f'{part2 = }')
                break

        if state in seen_states:
            continue
        seen_states.add(state)

        blizzards_new = []
        for b in blizzards:
            r, c, d = b
            r = (r + directions[d][0]) % len(grid)
            c = (c + directions[d][1]) % len(grid[0])
            blizzards_new.append((r, c, d))
        blizzards_new.sort()

        for d in directions:
            pn = (p[0]+directions[d][0], p[1]+directions[d][1])
            if pn == start or pn == end:
                state = (pn, tuple(blizzards_new))
                queue.append((state, i+1))
            if pn[0] < 0:
                continue
            if pn[0] > len(grid)-1:
                continue
            if pn[1] < 0:
                continue
            if pn[1] > len(grid[0])-1:
                continue
            if pn not in [(x[0], x[1]) for x in blizzards_new]:
                state = (pn, tuple(blizzards_new))
                queue.append((state, i+1))

    aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
