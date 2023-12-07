'''
Advent of Code 2023 - Day 7
'''
import aocd
from collections import defaultdict
from copy import deepcopy


def solve_a(input):
    ordering = "AKQJT98765432"
    winners = {
        "five_of_a_kind": [],
        "four_of_a_kind": [],
        "full_house": [],
        "three_of_a_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": []
    }
    bids = {}

    for line in input:
        cards, bid = line.split()
        bids[cards] = int(bid)
        cnt_cards = defaultdict(lambda: 0)
        for card in cards:
            cnt_cards[card] += 1
        if 5 in cnt_cards.values():
            winners["five_of_a_kind"].append(cards)
        elif 4 in cnt_cards.values():
            winners["four_of_a_kind"].append(cards)
        elif 3 in cnt_cards.values() and 2 in cnt_cards.values():
            winners["full_house"].append(cards)
        elif 3 in cnt_cards.values():
            winners["three_of_a_kind"].append(cards)
        elif list(cnt_cards.values()).count(2) == 2:
            winners["two_pair"].append(cards)
        elif 2 in cnt_cards.values():
            winners["one_pair"].append(cards)
        else:
            winners["high_card"].append(cards)

    return get_score(winners, ordering, bids)


def solve_b(input):
    ordering = "AKQT98765432J"
    winners = {
        "five_of_a_kind": [],
        "four_of_a_kind": [],
        "full_house": [],
        "three_of_a_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": []
    }
    bids = {}

    for line in input:
        cards, bid = line.split()
        bids[cards] = int(bid)
        highest_score = 0
        for c in ordering[:-1]:
            cp = deepcopy(cards)
            cp = cp.replace("J", c)
            cnt_cards = defaultdict(lambda: 0)
            for card in cp:
                cnt_cards[card] += 1
            if 5 in cnt_cards.values():
                highest_score = max(7, highest_score)
            elif 4 in cnt_cards.values():
                highest_score = max(6, highest_score)
            elif 3 in cnt_cards.values() and 2 in cnt_cards.values():
                highest_score = max(5, highest_score)
            elif 3 in cnt_cards.values():
                highest_score = max(4, highest_score)
            elif list(cnt_cards.values()).count(2) == 2:
                highest_score = max(3, highest_score)
            elif 2 in cnt_cards.values():
                highest_score = max(2, highest_score)
            else:
                highest_score = max(1, highest_score)

        match highest_score:
            case 7:
                winners["five_of_a_kind"].append(cards)
            case 6:
                winners["four_of_a_kind"].append(cards)
            case 5:
                winners["full_house"].append(cards)
            case 4:
                winners["three_of_a_kind"].append(cards)
            case 3:
                winners["two_pair"].append(cards)
            case 2:
                winners["one_pair"].append(cards)
            case 1:
                winners["high_card"].append(cards)

    return get_score(winners, ordering, bids)


def get_score(categories, ordering, bids):
    result = 0
    for c in categories:
        categories[c] = sorted(categories[c], key=lambda word: [ordering.index(c) for c in word])
    all = []
    for c in reversed(categories):
        all += reversed(categories[c])
    for i, item in enumerate(all):
        result += (i+1) * bids[item]
    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 7
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    part_a = solve_a(input)
    part_b = solve_b(input)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
