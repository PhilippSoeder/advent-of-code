'''
Advent of Code 2023 - Day 6
'''
import aocd


def get_ways_to_beat_record(race_durations, records):
    result = 1
    for i, time in enumerate(race_durations):
        record = records[i]
        ways_to_beat_record = 0
        beaten = False
        for j in range(time):
            d = j * (time - j)
            if d > record:
                ways_to_beat_record += 1
                beaten = True
            elif beaten and d <= record:
                break
        result *= ways_to_beat_record
        ways_to_beat_record = 0
    return result


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 6
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    race_durations = list(map(int, input[0].split(":")[1].strip().split()))
    records = list(map(int, input[1].split(":")[1].strip().split()))
    part_a = 1
    part_a *= get_ways_to_beat_record(race_durations, records)

    race_duration = [(int("".join(input[0].split(":")[1].strip().split())))]
    record = [(int("".join(input[1].split(":")[1].strip().split())))]
    part_b = 1
    part_b *= get_ways_to_beat_record(race_duration, record)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
