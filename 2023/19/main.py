'''
Advent of Code 2023 - Day 19
'''
import aocd


def solve_a(workflows, ratings):
    result = 0
    accepted = []

    for rating in ratings:
        workflow = "in"
        x = rating["x"]
        m = rating["m"]
        a = rating["a"]
        s = rating["s"]
        while True:
            if workflow == "R":
                break
            elif workflow == "A":
                accepted.append(rating)
                break
            for expr in workflows[workflow]:
                if ":" in expr:
                    if eval(expr.split(":")[0]):
                        workflow = expr.split(":")[1]
                        break
                else:
                    workflow = expr
    for rating in accepted:
        t = 0
        for i in rating:
            t += rating[i]
        result += t
    return result


def solve_b(workflows):
    result = 0
    states = [("in", 1, 4000, 1, 4000, 1, 4000, 1, 4000)]
    while len(states) > 0:
        workflow, xl, xh, ml, mh, al, ah, sl, sh = states.pop(0)
        if workflow == "R":
            continue
        elif workflow == "A":
            x = (xh - xl + 1)
            m = (mh - ml + 1)
            a = (ah - al + 1)
            s = (sh - sl + 1)
            result += x * m * a * s
        else:
            expressions = workflows[workflow]
            for expr in expressions:
                if ":" in expr:
                    cond, next_workflow = expr.split(":")
                    var = cond[0]
                    op = cond[1]
                    val = int(cond[2:])
                    new_intervals = get_new_intervals(var, op, val, False, xl, xh, ml, mh, al, ah, sl, sh)
                    states.append((next_workflow, *new_intervals))
                    xl, xh, ml, mh, al, ah, sl, sh = get_new_intervals(var, op, val, True, xl, xh, ml, mh, al, ah, sl, sh)
                else:
                    states.append((expr, xl, xh, ml, mh, al, ah, sl, sh))
    return result


def get_new_intervals(var, op, val, reversed, xl, xh, ml, mh, al, ah, sl, sh):
    if reversed:
        if op == "<":
            op = ">="
        elif op == ">":
            op = "<="
    if var == "x":
        xl, xh = get_new_interval(op, val, xl, xh)
    elif var == "m":
        ml, mh = get_new_interval(op, val, ml, mh)
    elif var == "a":
        al, ah = get_new_interval(op, val, al, ah)
    elif var == "s":
        sl, sh = get_new_interval(op, val, sl, sh)
    return xl, xh, ml, mh, al, ah, sl, sh


def get_new_interval(op, val, low, high):
    if op == "<":
        high = min(high, val - 1)
    elif op == "<=":
        high = min(high, val)
    elif op == ">":
        low = max(low, val + 1)
    elif op == ">=":
        low = max(low, val)
    return low, high


if __name__ == '__main__':
    AOC_YEAR = 2023
    AOC_DAY = 19
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

    workflows, ratings = input.split("\n\n")
    workflows = workflows.splitlines()
    workflows = {x.split("{")[0]: x.split("{")[1][:-1].split(",") for x in workflows}
    ratings = ratings.splitlines()
    ratings = [{y.split("=")[0]:int(y.split("=")[1]) for y in x[1:-1].split(",")} for x in ratings]

    part_a = solve_a(workflows, ratings)
    part_b = solve_b(workflows)

    print(f"{part_a = }")
    print(f"{part_b = }")

    aocd.submit(answer=part_a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=part_b, part='b', year=AOC_YEAR, day=AOC_DAY)
