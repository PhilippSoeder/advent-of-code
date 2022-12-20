'''
Advent of Code 2022 - Day 20
'''
import aocd


class Number:
    def __init__(self, number):
        self.number = number
        self.predecessor = None
        self.successor = None


def run(input, part2):
    inp = input
    if part2:
        inp = [x * 811589153 for x in inp]
    inp = [Number(x) for x in inp]
    for number in range(len(inp)):
        inp[number].predecessor = inp[(number - 1) % len(inp)]
        inp[number].successor = inp[(number + 1) % len(inp)]
    for _ in range(10):
        for a in inp:
            if a.number < 0:
                b = a
                for _ in range(-a.number % (len(inp) - 1)):
                    b = b.predecessor
                a.predecessor.successor = a.successor
                a.successor.predecessor = a.predecessor
                b.predecessor.successor = a
                a.predecessor = b.predecessor
                b.predecessor = a
                a.successor = b
            elif a.number > 0:
                b = a
                for _ in range(a.number % (len(inp) - 1)):
                    b = b.successor
                a.successor.predecessor = a.predecessor
                a.predecessor.successor = a.successor
                b.successor.predecessor = a
                a.successor = b.successor
                b.successor = a
                a.predecessor = b
            else:
                zero_index = a
                continue
        if not part2:
            break
    result = 0
    for _ in range(3):
        for _ in range(1000):
            zero_index = zero_index.successor
        result += zero_index.number
    return result


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 20
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    input = [int(x) for x in input]

    part1 = run(input, part2=False)
    part2 = run(input, part2=True)

    print(f'{part1 = }')
    print(f'{part2 = }')
    aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
