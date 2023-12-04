'''
Advent of Code 2023 - Day 4
'''
import aocd


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 4
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0

    cards = {}
    total_cards = []

    for card in input:
        card_id, numbers = card.split(":")
        card_id = int(card_id.split()[1])
        winning_numbers, own_numbers = numbers.split("|")
        winning_numbers = list(map(int, winning_numbers.split()))
        own_numbers = list(map(int, own_numbers.split()))
        own_winning_numbers = list(set(winning_numbers) & set(own_numbers))
        cards[card_id] = own_winning_numbers
        total_cards.append((card_id, own_winning_numbers))
        if len(own_winning_numbers) > 0:
            t = 1
            for w in range(len(own_winning_numbers) - 1):
                t *= 2
            part_a += t

    cnt_initial_cards = len(total_cards)

    change = True
    while change:
        change = False
        for c in total_cards:
            for w in range(len(c[1])):
                if c[0]+w+1 <= cnt_initial_cards:
                    total_cards.append((c[0]+w+1, cards[c[0]+w+1]))
                    changed = True
    part_b = len(total_cards)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
