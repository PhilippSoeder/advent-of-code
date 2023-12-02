'''
Advent of Code 2023 - Day 2
'''
import aocd


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 2
    input = open("input.txt").read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part_a = 0
    part_b = 0
    for line in input:
        green = []
        red = []
        blue = []
        game_id, subset_cubes = line.split(":")
        game_id = game_id.split(" ")[1]
        subset_cubes = [x.strip() for x in subset_cubes.split(";")]
        for revealed_cubes in subset_cubes:
            revealed_cubes = [x.strip() for x in revealed_cubes.split(",")]
            for i in revealed_cubes:
                cnt, color = i.split(" ")
                match color:
                    case "green":
                        green.append(int(cnt))
                    case "red":
                        red.append(int(cnt))
                    case "blue":
                        blue.append(int(cnt))

        if max(red) <= 12 and max(green) <= 13 and max(blue) <= 14:
            part_a += int(game_id)

        part_b += max(red) * max(green) * max(blue)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
