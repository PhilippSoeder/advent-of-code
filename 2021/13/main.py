'''
Advent of Code 2021 - Day 13
'''
import aocd


def fold(grid, fold_direction, line_number):
    if fold_direction == "y":
        a = grid[:line_number]
        b = grid[line_number + 1:][::-1]
    elif fold_direction == "x":
        a = []
        b = []
        for row in grid:
            a.append(row[:line_number])
            b.append(row[line_number + 1:][::-1])
    new_grid = []
    for r, row in enumerate(a):
        new_row = []
        for c, _ in enumerate(row):
            if a[r][c] == "#" or b[r][c] == "#":
                new_row.append("#")
            else:
                new_row.append(" ")
        new_grid.append(new_row)
    return new_grid


if __name__ == '__main__':
    AOC_YEAR = 2021
    AOC_DAY = 13
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)
    c_dots, instruct = input.split("\n\n")
    c_dots = c_dots.splitlines()
    instruct = instruct.splitlines()
    instruct = [i.replace("fold along ", "").split("=") for i in instruct]
    part_a = 0

    max_r = 0
    max_c = 0
    dots = []
    for dot in c_dots:
        c, r = list(map(int, dot.split(",")))
        max_r = max(max_r, r)
        max_c = max(max_c, c)
        dots.append((r, c))

    grid = []
    for r in range(max_r + 1):
        row = []
        for c in range(max_c + 1):
            row.append(" ")
        grid.append(row)

    for dot in dots:
        r, c = dot
        grid[r][c] = "#"

    for (fold_direction, line_number) in instruct:
        grid = fold(grid, fold_direction, int(line_number))
        if part_a == 0:
            for row in grid:
                part_a += row.count("#")

    print(f"{part_a = }")

    char_width = len(grid[0]) // 8
    char_middle = len(grid) // 2
    for r, row in enumerate(grid):
        if r == char_middle:
            print("part_b = ", end="")
        else:
            print("         ", end="")
        for c, char in enumerate(row):
            if c % char_width == 0 and c != 0:
                print("   ", end="")
            print(char, end="")
        print()

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
