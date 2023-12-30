'''
Advent of Code 2022 - Day 7
'''
import aocd


def part1() -> int:
    current_directory = ''
    current_folder = ''
    for line in input:
        a = line.split()
        match a[0]:
            case '$':
                match a[1]:
                    case 'cd':
                        if a[2] == '..':
                            tmp = current_directory.split('/')
                            tmp = [i for i in tmp if i]
                            tmp.pop()
                            if tmp != []:
                                current_directory = '/' + '/'.join(tmp) + '/'
                            else:
                                current_directory = '/'
                        else:
                            current_folder = a[2]
                            current_directory += current_folder
                            if a[2] != '/':
                                current_directory += '/'
                            if current_directory not in fs:
                                fs[current_directory] = {'file': False}
                    case 'ls':
                        pass
            case 'dir':
                pass
            case _:
                current_path = str(current_directory) + a[1]
                fs[current_path] = {'file': True, 'size': int(a[0])}

    for element in fs:
        if fs[element]['file']:
            tmp = str(element).split('/')
            tmp = [i for i in tmp if i]
            tmp.pop()
            if tmp != []:
                current_directory = '/' + '/'.join(tmp) + '/'
            else:
                current_directory = '/'
            if 'size' in fs[current_directory]:
                fs[current_directory]['size'] += fs[element]['size']
            else:
                fs[current_directory].update({'size': fs[element]['size']})

    folders = []
    for element in fs:
        if not fs[element]['file']:
            folders.append(element)

    folders = sorted(folders, key=lambda x: x.count('/'))
    folders = folders[::-1]

    for element in folders:
        if element != '/':
            tmp = str(element).split('/')
            tmp = [i for i in tmp if i]
            tmp.pop()
            if tmp != []:
                current_directory = '/' + '/'.join(tmp) + '/'
            else:
                current_directory = '/'
            if 'size' in fs[current_directory]:
                fs[current_directory]['size'] += fs[element]['size']
            else:
                fs[current_directory].update({'size': fs[element]['size']})

    t = 0
    for element in fs:
        if not fs[element]['file']:
            if fs[element]['size'] <= 100000:
                t += fs[element]['size']
    return t


def part2() -> int:
    total_disk_space = 70000000
    needed_unused = 30000000
    used = fs['/']['size']
    unused = total_disk_space - used
    needed = needed_unused - unused
    smallest = total_disk_space
    for element in fs:
        if not fs[element]['file']:
            if fs[element]['size'] >= needed:
                if fs[element]['size'] < smallest:
                    smallest = fs[element]['size']
    return smallest


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 7
    example = f"{AOC_YEAR}/{AOC_DAY}/input.txt"
    input = open(example).read().splitlines()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY).splitlines()

    fs = {}

    a = part1()
    b = part2()

    print(f'{a = }')
    print(f'{b = }')

    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)
