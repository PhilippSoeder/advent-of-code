'''
Advent of Code 2022 - Day 19
'''
import aocd
import re


def sim(ore_ore_c, cla_ore_c, obs_ore_c, obs_cla_c, geo_ore_c, geo_obs_c, t):
    geo_optimum = 0
    state = (1, 0, 0, 0, 0, 0, 0, 0, t)
    queue = [state]
    states_seen = set()
    while len(queue) > 0:
        state = queue.pop()
        ore_r, cla_r, obs_r, geo_r, ore, cla, obs, geo, t = state

        geo_optimum = max(geo_optimum, geo)

        if t < 1:
            continue

        # reducing possible states
        max_ore_c = max([ore_ore_c, cla_ore_c, obs_ore_c, geo_ore_c])
        if ore_r >= max_ore_c:
            ore_r = max_ore_c
        if cla_r >= obs_cla_c:
            cla_r = obs_cla_c
        if obs_r >= geo_obs_c:
            obs_r = geo_obs_c
        if ore >= max_ore_c * t - ore_r * (t - 1):
            ore = max_ore_c * t - ore_r * (t - 1)
        if cla >= obs_cla_c * t - cla_r * (t - 1):
            cla = obs_cla_c * t - cla_r * (t - 1)
        if obs >= geo_obs_c * t - obs_r * (t - 1):
            obs = geo_obs_c * t - obs_r * (t - 1)

        state = (
                    ore_r,
                    cla_r,
                    obs_r,
                    geo_r,
                    ore,
                    cla,
                    obs,
                    geo,
                    t
                )

        if state in states_seen:
            continue
        states_seen.add(state)

        # normal collection
        queue.append((
                        ore_r,
                        cla_r,
                        obs_r,
                        geo_r,
                        ore + ore_r,
                        cla + cla_r,
                        obs + obs_r,
                        geo + geo_r,
                        t - 1
                    ))
        if ore >= ore_ore_c:
            # buy ore robot + normal collection
            queue.append((
                            ore_r + 1,
                            cla_r,
                            obs_r,
                            geo_r,
                            ore - ore_ore_c + ore_r,
                            cla + cla_r,
                            obs + obs_r,
                            geo + geo_r,
                            t - 1
                        ))
        if ore >= cla_ore_c:
            # buy clay robot + normal collection
            queue.append((
                            ore_r,
                            cla_r + 1,
                            obs_r,
                            geo_r,
                            ore - cla_ore_c + ore_r,
                            cla + cla_r,
                            obs + obs_r,
                            geo + geo_r,
                            t - 1
                        ))
        if ore >= obs_ore_c and cla >= obs_cla_c:
            # buy obsidian robot + normal collection
            queue.append((
                            ore_r,
                            cla_r,
                            obs_r + 1,
                            geo_r,
                            ore - obs_ore_c + ore_r,
                            cla - obs_cla_c + cla_r,
                            obs + obs_r,
                            geo + geo_r,
                            t - 1
                        ))
        if ore >= geo_ore_c and obs >= geo_obs_c:
            # buy geode robot + normal collection
            queue.append((
                            ore_r,
                            cla_r,
                            obs_r,
                            geo_r + 1,
                            ore - geo_ore_c + ore_r,
                            cla + cla_r,
                            obs - geo_obs_c + obs_r,
                            geo + geo_r,
                            t - 1
                        ))
    return geo_optimum


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 19
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()
    part1 = 0
    part2 = 1

    for line in input:
        id, a, b, c, d, e, f = map(int, re.findall("\\d+", line))
        p1 = sim(a, b, c, d, e, f, 24)
        part1 += p1 * id
        if id <= 3:
            p2 = sim(a, b, c, d, e, f, 32)
            part2 *= p2

    print(f'{part1 = }')
    print(f'{part2 = }')

    aocd.submit(answer=part1, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part2, part='b', year=AOC_YEAR, day=AOC_DAY)
