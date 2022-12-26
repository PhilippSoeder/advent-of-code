'''
Advent of Code 2022 - Day 1
'''


def get_list_of_calories() -> list:
    with open("input.txt") as input:
        lines = input.read().splitlines()
    lines.append('')
    tmp_count = 0
    calories_list = []
    for line in lines:
        if line != '':
            tmp_count += int(line)
        else:
            calories_list.append(tmp_count)
            tmp_count = 0
    return calories_list


def part1(calories_list: list) -> int:
    return max(calories_list)


def part2(calories_list: list) -> int:
    calories_list.sort(reverse=True)
    return sum(calories_list[:3])


if __name__ == '__main__':
    calories_list = get_list_of_calories()
    print(f'Part 1: {part1(calories_list)}')
    print(f'Part 2: {part2(calories_list)}')
