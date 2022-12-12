'''
Advent of Code 2022 - Day 12
'''
import aocd


def char_to_int(char):
    return ord(char) - ord('a') + 1


def is_outside_map(r, c):
    if r < 0 or r >= len(map):
        return True
    if c < 0 or c >= len(map[0]):
        return True
    return False


def get_steps_to_end(start):
    Nodes = []
    Nodes.append((start[0], start[1], 0))
    visited = {start: True}
    while len(Nodes) > 0:
        r, c, d = Nodes.pop(0)
        for r_next, c_next in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if is_outside_map(r_next, c_next) or (r_next, c_next) in visited:
                continue
            if char_to_int(map[r_next][c_next]) - char_to_int(map[r][c]) > 1:
                continue
            if (r_next, c_next) == end:
                return d + 1
            Nodes.append((r_next, c_next, d + 1))
            visited[(r_next, c_next)] = True
    return None


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 12
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    map = []
    for r, line in enumerate(input):
        row = []
        for c, char in enumerate(line):
            if char == 'S':
                start = (r, c)
                row.append('a')
            elif char == 'E':
                end = (r, c)
                row.append('z')
            else:
                row.append(char)
        map.append(row)

    a = get_steps_to_end(start)
    print(f'{a = }')

    starting_points = []
    for r, _ in enumerate(map):
        for c, _ in enumerate(map[0]):
            if map[r][c] == 'a':
                starting_points.append((r, c))

    t = []
    for starting_point in starting_points:
        t.append(get_steps_to_end(starting_point))
    t = [x for x in t if type(x) == int]
    t.sort()

    b = t[0]
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
