'''
Advent of Code 2022 - Day 21
'''
import aocd
from sympy.solvers import solve
from sympy import Symbol


def calculate_result(monkey, part2):
    if type(monkeys[monkey]) == int:
        if monkey == 'humn' and part2:
            return 'x'
        return str(monkeys[monkey])
    else:
        a = calculate_result(monkeys[monkey]['a'], part2)
        b = calculate_result(monkeys[monkey]['b'], part2)
        o = monkeys[monkey]['o']
        if not part2 and monkey == 'root':
            global left
            global right
            left = a
            right = b
        elif part2 and monkey == 'root':
            x = Symbol('x')
            if left == a:
                func = f'{b} - {a}'
            if right == b:
                func = f'{a} - {b}'
            return solve(func, x)
        return f'({a} {o} {b})'


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 21
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part1 = 0
    part2 = 0

    monkeys = {}
    for line in input:
        monkey, job = line.split(':')
        if len(list(job.split())) == 1:
            monkeys[monkey] = int(job)
        else:
            a, o, b = job.split()
            monkeys[monkey] = {
                'o': o,
                'a': a,
                'b': b
            }

    part1 = int(eval(calculate_result('root', part2=False)))

    monkeys['humn'] += 1
    global left
    global right
    part2 = calculate_result('root', part2=True)[0]

    print(f'{part1 = }')
    print(f'{part2 = }')

    aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
