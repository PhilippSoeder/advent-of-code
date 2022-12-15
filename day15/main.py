'''
Advent of Code 2022 - Day 15
'''
import aocd


def md(p1, p2):
    d = 0
    for x1, x2 in zip(p1, p2):
        diff = x2 - x1
        abs_diff = abs(diff)
        d += abs_diff
    return d


def run(search_bound, part_a):
    for i in range(search_bound, -1, -1):
        sensor_ranges = []
        for j, sensor in enumerate(sensors):
            offset = ds[j] - abs(sensor[1] - i)
            if offset < 0:
                continue
            lower_bound = sensor[0] - offset
            upper_bound = sensor[0] + offset
            sensor_ranges.append([lower_bound, upper_bound])
        sensor_ranges.sort()

        range_list = []
        for sensor_range in sensor_ranges:
            if len(range_list) == 0:
                range_list.append(sensor_range)
                continue
            next_sensor_range = range_list[-1]

            if sensor_range[0] > next_sensor_range[1] + 1:
                range_list.append(sensor_range)
                continue

            range_list[-1][1] = max(next_sensor_range[1], sensor_range[1])

        if part_a:
            beacons_in_line = set()
            for beacon in beacons:
                if beacon[1] == search_bound:
                    beacons_in_line.add(beacon)
            not_possible = abs(range_list[0][0]) + abs(range_list[0][1]) + 1
            return not_possible - len(beacons_in_line)

        x = 0
        for sensor_range in range_list:
            if x < sensor_range[0]:
                return x * 4000000 + i
            x = max(x, sensor_range[1] + 1)
            if x > search_bound:
                break


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 15
    input = open("input.txt").read().splitlines()
    target_line_a = 10
    search_bound_b = 20
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    target_line_a = 2000000
    search_bound_b = 4000000

    sensors = []
    ds = []
    beacons = []
    for line in input:
        _, _, x_sensor, y_sensor, _, _, _, _, x_beacon, y_beacon = line.split()
        x_sensor = int(x_sensor.split('=')[1][:-1])
        y_sensor = int(y_sensor.split('=')[1][:-1])
        x_beacon = int(x_beacon.split('=')[1][:-1])
        y_beacon = int(y_beacon.split('=')[1])
        d = md((x_sensor, y_sensor), (x_beacon, y_beacon))
        sensors.append((x_sensor, y_sensor))
        beacons.append((x_beacon, y_beacon))
        ds.append(d)

    a = run(target_line_a, part_a=True)
    print(f'{a = }')
    b = run(search_bound_b, part_a=False)
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
