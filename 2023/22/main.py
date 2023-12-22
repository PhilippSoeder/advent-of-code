'''
Advent of Code 2023 - Day 22
'''
import aocd
from copy import deepcopy


def fall(bricks):
    moved_bricks = set()
    known_blocks = set()
    for brick in bricks:
        for block in brick:
            known_blocks.add(block)
    while True:
        moved = False
        for b, brick in enumerate(bricks):
            movable = True
            for x, y, z in brick:
                if z == 1:
                    movable = False
                    break
                if (x, y, z-1) in known_blocks and (x, y, z-1) not in brick:
                    movable = False
                    break
            if movable:
                moved_bricks.add(b)
                moved = True
                for (x, y, z) in brick:
                    known_blocks.remove((x, y, z))
                    known_blocks.add((x, y, z-1))
                bricks[b] = [(x, y, z-1) for (x, y, z) in brick]
        if not moved:
            return len(moved_bricks)


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 22
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0

    bricks = []
    for line in input:
        brick = []
        end1, end2 = line.split("~")
        x1, y1, z1 = list(map(int, end1.split(",")))
        x2, y2, z2 = list(map(int, end2.split(",")))
        # Assumption 1 is always lower or equal compared to 2
        assert x1 <= x2
        assert y1 <= y2
        assert z1 <= z2
        if x1 == x2 and y1 == y2:
            for z in range(z1, z2+1):
                brick.append((x1, y1, z))
        elif x1 == x2 and z1 == z2:
            for y in range(y1, y2+1):
                brick.append((x1, y, z1))
        elif y1 == y2 and z1 == z2:
            for x in range(x1, x2+1):
                brick.append((x, y1, z1))
        bricks.append(brick)

    fall(bricks)

    for b, brick in enumerate(bricks):
        bricks_copy = deepcopy(bricks)
        bricks_copy.pop(b)
        bricks_moved = fall(bricks_copy)
        part_b += bricks_moved
        if bricks_moved == 0:
            part_a += 1

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
