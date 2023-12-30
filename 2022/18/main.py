'''
Advent of Code 2022 - Day 18
'''
import aocd


def part1():
    connected_sides = 0
    for i in range(len(lava)-1):
        for j in range(i+1, len(x)):
            cube_1 = (x[i], y[i], z[i])
            cube_2 = (x[j], y[j], z[j])
            coordinates_same = 0
            coordinates_one_off = 0
            for k in range(3):
                if cube_1[k] == cube_2[k]:
                    coordinates_same += 1
                else:
                    if abs(cube_1[k] - cube_2[k]) == 1:
                        coordinates_one_off += 1
            if coordinates_one_off == 1 and coordinates_same == 2:
                connected_sides += 2
    return len(lava) * 6 - connected_sides


def part2():
    air = set()
    for i in range(min_x-1, max_x+2):
        for j in range(min_y-1, max_y+2):
            for k in [min_z-1, max_z+1]:
                air.add((i, j, k))
    for i in [min_x-1, max_x+1]:
        for j in range(min_y-1, max_y+2):
            for k in range(min_z-1, max_z+2):
                air.add((i, j, k))
    for i in range(min_x-1, max_x+2):
        for j in [min_y-1, max_y+1]:
            for k in range(min_z-1, max_z+2):
                air.add((i, j, k))

    queue = []
    for item in air:
        queue.append(item)

    b = 0
    visited = set()
    while len(queue) > 0:
        element = queue.pop(0)
        if element[0] < min_x-1 or element[0] > max_x+1:
            continue
        if element[1] < min_y-1 or element[1] > max_y+1:
            continue
        if element[2] < min_z-1 or element[2] > max_z+1:
            continue
        if element in visited:
            continue
        if element in lava:
            b += 1
            continue
        visited.add(element)
        for o in offset:
            dx = element[0]+o[0]
            dy = element[1]+o[1]
            dz = element[2]+o[2]
            queue.append((dx, dy, dz))
    return b


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 18
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    lava = []
    x, y, z = [], [], []
    offset = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]

    for line in input:
        x1, y1, z1 = map(int, line.split(','))
        x.append(x1)
        y.append(y1)
        z.append(z1)
        lava.append((x1, y1, z1))

    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)
    min_z = min(z)
    max_z = max(z)

    a = part1()
    b = part2()

    print(f'{a = }')
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
