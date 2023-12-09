'''
Advent of Code 2023 - Day 9
'''
import aocd


def solve(input, important_element_position):
    result = 0
    for element in input:
        history = [list(map(int, element.split()))]
        line = 0
        while any(history[line]):
            next_line = []
            for i in range(len(history[line]) - 1):
                next_line.append(history[line][i+1] - history[line][i])
            history.append(next_line)
            line += 1
        history[line].append(0)
        history[line-1].append(history[line-1][-1])
        for i in reversed(range(len(history) - 2)):
            if important_element_position == -1:  # part a
                history[i].append(history[i][-1] + history[i+1][-1])
            elif important_element_position == 0:  # part b
                history[i] = [history[i][0] - history[i+1][0]] + history[i]
        result += history[0][important_element_position]
    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 9
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    part_a = solve(input, important_element_position=-1)
    part_b = solve(input, important_element_position=0)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
