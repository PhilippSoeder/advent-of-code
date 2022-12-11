'''
Advent of Code 2022 - Day 11
'''
import aocd


def simulate_rounds(rounds, part1):
    monkeys = []
    for line in input:
        line = line.strip()
        if line.startswith(STR_MONKEY):
            monkey = {}
        elif line.startswith(STR_STARTING_ITEMS):
            monkey['items'] = list(map(int, line.split(':')[1].split(',')))
        elif line.startswith(STR_OPERATION):
            monkey['operation'] = eval('lambda old:' + line.split('=')[1])
        elif line.startswith(STR_TEST):
            monkey['test'] = int(line.split()[-1])
        elif line.startswith(STR_TEST_TRUE):
            monkey['true'] = int(line.split()[-1])
        elif line.startswith(STR_TEST_FALSE):
            monkey['false'] = int(line.split()[-1])
            monkeys.append(monkey)

    inspections = [0 for _ in range(len(monkeys))]

    multipied_divisor = 1
    for monkey in monkeys:
        multipied_divisor *= monkey['test']

    for _ in range(rounds):
        for m, monkey in enumerate(monkeys):
            for i, item in enumerate(monkey['items']):
                monkey['items'][i] = monkey['operation'](item)
                inspections[m] += 1
                if part1:
                    monkey['items'][i] = int(monkey['items'][i] / 3)
                monkey['items'][i] = monkey['items'][i] % multipied_divisor
                if monkey['items'][i] % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(monkey['items'][i])
                else:
                    monkeys[monkey['false']]['items'].append(monkey['items'][i])
            monkeys[m]['items'] = []

    inspections.sort()
    return inspections[-1] * inspections[-2]


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 11
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    STR_MONKEY = 'Monkey'
    STR_STARTING_ITEMS = 'Starting items'
    STR_OPERATION = 'Operation'
    STR_TEST = 'Test'
    STR_TEST_TRUE = 'If true'
    STR_TEST_FALSE = 'If false'

    a = simulate_rounds(20, part1=True)
    print(f'{a = }')

    b = simulate_rounds(10000, part1=False)
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
