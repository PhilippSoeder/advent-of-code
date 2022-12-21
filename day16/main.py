'''
Advent of Code 2022 - Day 16
'''
import aocd
from collections import deque


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 16
    input = open("input.txt").read().splitlines()
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
        to_valves = [x[:2] for x in words[9:]]
        pipe['to_valves'] = to_valves
        pipes[valve] = pipe

    ''' 
    TODO:   optimize input by removing valves with 0 flow
            and add cost to travel to all other valves to
            that valve.
            Only a small number of valves have flow > 0.
            Leave 'AA' in the list, since it it the start.
    '''

    states_seen = set()
    state = ('AA', (), 0, 30)
    queue = deque([state])
    while len(queue) > 0:
        state = queue.pop()
        cp, ov, flow, t = state
        a = max(a, flow)
        if t <= 0:
            continue
        if state in states_seen:
            continue
        states_seen.add(state)

        for d in pipes[cp]['to_valves']:
            state = (d, ov, flow, t-1)
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
