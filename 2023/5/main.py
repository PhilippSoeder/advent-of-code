'''
Advent of Code 2023 - Day 5
'''
import aocd


def solve_a(seeds, mappings):
    to_check = seeds
    for mapping in mappings:
        ranges = []
        for line in mapping.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        next = []
        for i in to_check:
            found = False
            for r in ranges:
                if i >= r[1] and i < r[1]+r[2]:
                    next.append(r[0]+i-r[1])
                    found = True
            if not found:
                next.append(i)
        to_check = next
    return min(to_check)


def solve_b(seeds, mappings):
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]))
    to_check = seed_ranges
    for mapping in mappings:
        ranges = []
        for line in mapping.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        next = []
        while len(to_check) > 0:
            found = False
            start_range, end_range = to_check.pop()
            for drs, srs, rl in ranges:
                start_overlap = max(start_range, srs)
                end_overlap = min(end_range, srs+rl)
                if start_overlap < end_overlap:
                    next.append((start_overlap-srs+drs, end_overlap-srs+drs))
                    found = True
                    if start_overlap > start_range:
                        to_check.append((start_range, start_overlap))
                    if end_range > end_overlap:
                        to_check.append((end_overlap, end_range))
            if not found:
                next.append((start_range, end_range))
        to_check = next
    return min(to_check)[0]


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 5
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    seeds, *mappings = open(example).read().split("\n\n")
    seeds, *mappings = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).split("\n\n")
    seeds = list(map(int, seeds.split(": ")[1].split()))

    part_a = solve_a(seeds, mappings)
    part_b = solve_b(seeds, mappings)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
