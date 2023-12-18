'''
Advent of Code 2023 - Day 18
'''
import aocd


def solve(dig_plan, part):
    r = 0
    c = 0
    border = 0
    marked = []
    for instruction in dig_plan:
        if part == "a":
            direction, amount, _ = instruction
        elif part == "b":
            _, _, hexcode = instruction
            a = hexcode[:-1]
            amount = int(a, 16)
            d = hexcode[-1]
            match d:
                case "0":
                    direction = "R"
                case "1":
                    direction = "D"
                case "2":
                    direction = "L"
                case "3":
                    direction = "U"
        border += amount
        match direction:
            case "U":
                for _ in range(amount):
                    marked.append((r, c))
                    r -= 1
            case "R":
                for _ in range(amount):
                    marked.append((r, c))
                    c += 1
            case "D":
                for _ in range(amount):
                    marked.append((r, c))
                    r += 1
            case "L":
                for _ in range(amount):
                    marked.append((r, c))
                    c -= 1

    # https://en.wikipedia.org/wiki/Shoelace_formula
    x = sum(marked[i][0] * (marked[i-1][1] - marked[(i+1) % len(marked)][1])
            for i in range(len(marked)))
    shoelace = abs(x) // 2

    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    pick = shoelace - border // 2 + 1

    return pick + border


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 18
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    dig_plan = []
    for line in input:
        direction, amount, color = line.split()
        dig_plan.append((direction, int(amount), color[2:-1]))

    part_a = solve(dig_plan, "a")
    part_b = solve(dig_plan, "b")

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
