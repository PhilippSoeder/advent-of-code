'''
Advent of Code 2023 - Day 13
'''
import aocd


def solve(input, part):
    result = 0

    if part == "a":
        needed_fails = 0
    elif part == "b":
        needed_fails = 1

    patterns = input.split("\n\n")

    for pattern in patterns:
        pattern = [[x for x in pattern] for pattern in pattern.splitlines()]

        # horizontal check
        for r1 in range(len(pattern) - 1):
            fails = 0
            for r2 in range(len(pattern)):
                up = r1 - r2
                down = r1 + 1 + r2
                if 0 <= up < down < len(pattern):
                    for c in range(len(pattern[0])):
                        if pattern[up][c] != pattern[down][c]:
                            fails += 1
            if fails == needed_fails:
                result += 100 * (r1 + 1)

        # vertical check
        for c1 in range(len(pattern[0]) - 1):
            fails = 0
            for c2 in range(len(pattern[0])):
                left = c1 - c2
                right = c1 + 1 + c2
                if 0 <= left < right < len(pattern[0]):
                    for r in range(len(pattern)):
                        if pattern[r][left] != pattern[r][right]:
                            fails += 1
            if fails == needed_fails:
                result += c1 + 1

    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 13
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

    part_a = solve(input, "a")
    part_b = solve(input, "b")

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
