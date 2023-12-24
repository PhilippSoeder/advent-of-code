'''
Advent of Code 2023 - Day 24
'''
import aocd
from itertools import combinations
import numpy as np
from z3 import Int, Solver, sat


def solve_a(hailstones, low, high):
    result = 0
    for h1, h2 in combinations(hailstones, 2):
        x1, y1, _, vx1, vy1, _ = h1
        x2, y2, _, vx2, vy2, _ = h2
        m1 = vy1 / vx1
        m2 = vy2 / vx2
        if m1 == m2:
            continue
        a1 = np.array([[m1, -1], [m2, -1]])
        a2 = np.array([m1 * x1 - y1, m2 * x2 - y2])
        x, y = np.linalg.solve(a1, a2)
        if low <= x <= high and low <= y <= high:
            t1 = (x - x1) / vx1
            t2 = (x - x2) / vx2
            if t1 > 0 and t2 > 0:
                result += 1
    return result


def solve_b(hailstones):
    solver = Solver()
    x, y, z, vx, vy, vz = map(Int, ('x', 'y', 'z', 'vx', 'vy', 'vz'))
    for i, (a, b, c, va, vb, vc) in enumerate(hailstones[:3]):
        t = Int(f"t{i}")
        solver.add(t > 0)
        solver.add(x + vx * t == a + va * t)
        solver.add(y + vy * t == b + vb * t)
        solver.add(z + vz * t == c + vc * t)
    if solver.check() == sat:
        model = solver.model()
        return sum(model.eval(n).as_long() for n in (x, y, z))


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 24
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    low, high = 7, 27
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    low, high = 200000000000000, 400000000000000

    hailstones = []
    for line in input:
        line = line.replace("@", ",")
        px, py, pz, vx, vy, vz = list(map(int, line.split(", ")))
        hailstones.append([px, py, pz, vx, vy, vz])

    part_a = solve_a(hailstones, low, high)
    part_b = solve_b(hailstones)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
