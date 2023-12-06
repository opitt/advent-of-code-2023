# https://adventofcode.com/2023/day/5
import os
import re
from collections import namedtuple

Fromto = namedtuple("Fromto", "dest_min dest_max src_min src_max")


def solve(lines):
    def find_location(seed, almanac):
        thing = seed
        for almanac_line in almanac:
            for fromto in almanac_line:
                # if no mapping found, then dest has the same value as sourc
                if fromto.src_min <= thing <= fromto.src_max:
                    thing = fromto.dest_min + thing - fromto.src_min
                    break
        return thing

    seeds = list(map(int, lines[0].split()[1:]))
    mapping = []
    for line in lines[2:]:
        if line == "":
            continue
        if re.match("[a-z].+", line):
            mapping.append([])
        else:
            dest, src, length = map(int, line.split())
            mapping[-1].append(Fromto(dest, dest + length - 1, src, src + length - 1))

    locations = [find_location(seed, mapping) for seed in seeds]

    return min(locations)


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines)
    print(f"The result is {result}.")
    # 993500720


# main(test=True)
main(test=False)
