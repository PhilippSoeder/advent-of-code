'''
Advent of Code 2023 - Day 20
'''
import aocd
from math import gcd


def push_button(count):
    global low_pulses
    global high_pulses
    q = []
    low_pulses += 1
    # print(f"button -low-> broadcaster")
    for dest in modules["broadcaster"]["destinations"]:
        q.append(("low", dest, "broadcaster"))
        low_pulses += 1
        # print(f"broadcaster -low-> {dest}")

    while len(q) > 0:
        pulse, module, from_module = q.pop(0)
        if module not in modules:
            continue
        if modules[module]["type"] == "flip-flop" and pulse == "low":
            modules[module]["active"] = not modules[module]["active"]
            if modules[module]["active"]:
                for dest in modules[module]["destinations"]:
                    q.append(("high", dest, module))
                    high_pulses += 1
                    # print(f"{module} -high-> {dest}")
            else:
                for dest in modules[module]["destinations"]:
                    q.append(("low", dest, module))
                    low_pulses += 1
                    # print(f"{module} -low-> {dest}")
        elif modules[module]["type"] == "conjunction module":
            # only relevant for part b START
            if module == "vd" and pulse == "high" \
               and vd_inputs_count_until_high[from_module] is None:
                vd_inputs_count_until_high[from_module] = count
            # only relevant for part b END
            modules[module]["inputs"][from_module] = pulse
            if set(modules[module]["inputs"].values()) == {"high"}:
                for dest in modules[module]["destinations"]:
                    q.append(("low", dest, module))
                    low_pulses += 1
                    # print(f"{module} -low-> {dest}")
            else:
                for dest in modules[module]["destinations"]:
                    q.append(("high", dest, module))
                    high_pulses += 1
                    # print(f"{module} -high-> {dest}")


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 20
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    modules = {}
    for line in input:
        module, destinations = line.split(" -> ")
        destinations = destinations.split(", ")
        if module == "broadcaster":
            modules[module] = {
                "type": "broadcaster",
                "destinations": destinations
                }
        elif module.startswith("%"):
            modules[module[1:]] = {
                "type": "flip-flop",
                "destinations": destinations,
                "active": False
            }
        elif module.startswith("&"):
            modules[module[1:]] = {
                "type": "conjunction module",
                "destinations": destinations,
                "inputs": {}
            }

    for module in modules:
        if modules[module]["type"] == "conjunction module":
            for module2 in modules:
                if module in modules[module2]["destinations"]:
                    modules[module]["inputs"][module2] = "low"

    # part_b: rx has only one input: vd, which is a conjunction module
    # rx will receive a low pulse if all vd inputs are high
    # lcm is used to get number of presses until all vd inputs are high
    vd_inputs_count_until_high = {}
    for module in modules:
        if "vd" in modules[module]["destinations"]:
            vd_inputs_count_until_high[module] = None

    part_a = None
    part_b = None
    low_pulses = 0
    high_pulses = 0
    count = 0
    while True:
        count += 1
        push_button(count)
        if count == 1000:
            part_a = low_pulses * high_pulses
        if part_b is None and None not in vd_inputs_count_until_high.values():
            # all inputs of vd have been at least once high
            # now we can use lcm to get answer for part b
            part_b = 1
            for number in vd_inputs_count_until_high.values():
                part_b = part_b * number // gcd(part_b, number)
        if part_a is not None and part_b is not None:
            break

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
