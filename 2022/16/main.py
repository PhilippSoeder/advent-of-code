'''
Advent of Code 2022 - Day 16
'''
import sys
import aocd
from collections import deque


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 16
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    a = 0
    b = 0

    pipes = {}
    for line in input:
        pipe = {}
        words = line.split()
        valve = words[1]
        flow_rate = int(words[4].split('=')[1][:-1])
        pipe['flow_rate'] = flow_rate
        direct_connections = [x[:2] for x in words[9:]]
        pipe['direct_connections'] = direct_connections
        pipes[valve] = pipe

    non_zero_flow = [x for x in pipes if pipes[x]['flow_rate'] > 0]

    for valve in pipes:
        pipes[valve]['connections'] = dict()
        for x in non_zero_flow:
            if x == valve:
                continue
            pipes[valve]['connections'][x] = sys.maxsize
            queue = deque([[valve, 0]])
            visited = set()
            while len(queue) > 0:
                item, distance = queue.popleft()
                if item in visited:
                    continue
                visited.add(item)
                for v in pipes[item]['direct_connections']:
                    if v == x:
                        best = min(distance+1, pipes[valve]['connections'][x])
                        pipes[valve]['connections'][x] = best
                    else:
                        queue.append([v, distance+1])

    states_seen = set()
    state = ('AA', (), 0, 30)
    queue = deque([state])
    while len(queue) > 0:
        state = queue.popleft()
        cp, ov, flow, t = state
        a = max(a, flow)
        if t <= 0:
            continue
        if state in states_seen:
            continue
        states_seen.add(state)

        for item in pipes[cp]['connections']:
            state = (item, ov, flow, t-pipes[cp]['connections'][item])
            queue.append(state)

        if pipes[cp]['flow_rate'] > 0:
            ov = list(ov)
            if cp not in ov:
                flow += pipes[cp]['flow_rate'] * (t-1)
                ov.append(cp)
                ov.sort()
                state = (cp, tuple(ov), flow, t-1)
                queue.append(state)

    print(f'{a = }')
    #print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    #aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
