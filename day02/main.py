'''
Advent of Code 2022 - Day 2
'''


def get_plays() -> list:
    with open("input.txt") as input:
        return input.read().splitlines()


def part1() -> int:
    total = 0
    for play in plays:
        hint = play.split(' ')
        if hint[1] == need_for_win[hint[0]]:
            total += win[hint[0]]
        elif hint[1] == need_for_draw[hint[0]]:
            total += draw[hint[0]]
        elif hint[1] == need_for_lose[hint[0]]:
            total += lose[hint[0]]
    return total


def part2() -> int:
    total = 0
    for play in plays:
        hint = play.split(' ')
        if hint[1] == "Z":
            total += win[hint[0]]
        elif hint[1] == "Y":
            total += draw[hint[0]]
        elif hint[1] == "X":
            total += lose[hint[0]]
    return total


if __name__ == '__main__':
    need_for_win = {"A": "Y", "B": "Z", "C": "X"}
    need_for_draw = {"A": "X", "B": "Y", "C": "Z"}
    need_for_lose = {"A": "Z", "B": "X", "C": "Y"}

    win = {"A": 8, "B": 9, "C": 7}
    draw = {"A": 4, "B": 5, "C": 6}
    lose = {"A": 3, "B": 1, "C": 2}

    plays = get_plays()

    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
