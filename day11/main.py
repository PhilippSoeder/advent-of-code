'''
Advent of Code 2022 - Day 11
'''
import aocd


def simulate_rounds(rounds, part1):
    monkeys = []
    for line in input:
        if line.startswith(STR_MONKEY):
            monkey = {}
            monkey['inspections'] = 0
        elif line.startswith(STR_STARTING_ITEMS):
            line = line[len(STR_STARTING_ITEMS):]
            items = line.split(', ')
            items = list(map(int, items))
            monkey['items'] = items
        elif line.startswith(STR_OPERATION):
            line = line[len(STR_OPERATION):]
            operation = line.split()
            for i, element in enumerate(operation):
                if element.isdigit():
                    operation[i] = int(element)
            monkey['operation'] = operation
        elif line.startswith(STR_TEST):
            test = line[len(STR_TEST):]
            test = int(test)
            monkey['test'] = test
        elif line.startswith(STR_TEST_TRUE):
            true = line[len(STR_TEST_TRUE):]
            true = int(true)
            monkey['true'] = true
        elif line.startswith(STR_TEST_FALSE):
            false = line[len(STR_TEST_FALSE):]
            false = int(false)
            monkey['false'] = false
            monkeys.append(monkey)

    multipied_divisor = 1
    for monkey in monkeys:
        multipied_divisor *= monkey['test']

    for _ in range(1, rounds + 1):
        for m, monkey in enumerate(monkeys):
            items_to_remove = []
            for i, item in enumerate(monkey['items']):
                monkey['items'][i] = inspect_item(item, monkey['operation'])
                monkeys[m]['inspections'] += 1
                if part1:
                    monkey['items'][i] = int(monkey['items'][i] / 3)
                monkey['items'][i] = monkey['items'][i] % multipied_divisor
                if monkey['items'][i] % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(monkey['items'][i])
                else:
                    monkeys[monkey['false']]['items'].append(monkey['items'][i])
                items_to_remove.append(i)
            new_items = []
            for i, item in enumerate(monkeys[m]['items']):
                if i not in items_to_remove:
                    new_items.append(item)
            monkeys[m]['items'] = new_items

    most_active = [0, 0]

    for monkey in monkeys:
        if monkey['inspections'] > min(most_active):
            most_active = [max(most_active), monkey['inspections']]
    return most_active[0] * most_active[1]


def inspect_item(item, operation):
    if operation[1] == 'old':
        n = item
    else:
        n = operation[1]
    match operation[0]:
        case '+':
            return item + n
        case '*':
            return item * n


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 11
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    STR_MONKEY = 'Monkey '
    STR_STARTING_ITEMS = '  Starting items: '
    STR_OPERATION = '  Operation: new = old '
    STR_TEST = '  Test: divisible by '
    STR_TEST_TRUE = '    If true: throw to monkey '
    STR_TEST_FALSE = '    If false: throw to monkey '

    a = simulate_rounds(20, part1=True)
    print(f'{a = }')

    b = simulate_rounds(10000, part1=False)
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
