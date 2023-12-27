'''
Advent of Code 2021 - Day 10
'''
import aocd


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 10
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0

    points = {
        ")": (3, 1),
        "]": (57, 2),
        "}": (1197, 3),
        ">": (25137, 4)
    }

    matching = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    scores = []

    for line in input:
        stack = []
        for character in line:
            match character:
                case "(" | "[" | "{" | "<":
                    stack.append(character)
                case ")" | "]" | "}" | ">":
                    last = stack.pop()
                    if matching[last] != character:
                        part_a += points[character][0]
                        break
        else:
            score = 0
            while len(stack) > 0:
                last = stack.pop()
                score *= 5
                score += points[matching[last]][1]
            scores.append(score)
    part_b = sorted(scores)[len(scores) // 2]

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
