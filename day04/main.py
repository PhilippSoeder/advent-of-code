'''
Advent of Code 2022 - Day 4
'''
import aocd


def a() -> int:
    result = 0
    for line in input:
        unionset = set(line[0]).union(set(line[1]))
        if unionset == set(line[0]):
            result += 1
        elif unionset == set(line[1]):
            result += 1
    return result


def b() -> int:
    result = 0
    for line in input:
        overlap = False
        for element in line[0]:
            if element in line[1]:
                overlap = True
        for element in line[1]:
            if element in line[0]:
                overlap = True
        if overlap:
            result += 1
    return result


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 4
    # input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    input = [line.split(',') for line in input]
    input_tmp = []
    for line in input:
        input_tmp += [row.split('-') for row in line]
    input = input_tmp
    input_tmp = []
    for i in range(0, len(input), 2):
        first_range = range(int(input[i][0]), int(input[i][1])+1)
        first_list = []
        second_range = range(int(input[i+1][0]), int(input[i+1][1])+1)
        second_list = []
        for i in first_range:
            first_list.append(i)
        for j in second_range:
            second_list.append(j)
        input_tmp.append([first_list, second_list])
    input = input_tmp
    a = a()
    print(f'{a = }')
    b = b()
    print(f'{b = }')
    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
