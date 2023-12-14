# https://adventofcode.com/2023/day/5
import os
import re
import datetime as dt
from collections import namedtuple
from copy import deepcopy

Fromto = namedtuple("Fromto", "a b to_a to_b")


def solve(lines):
    def trans(seeds, intervalls):
        result = []
        for seed_a, seed_b in seeds:
            # map all seed intervalls to the almanach intervalls fromto
            for fromto in intervalls:
                if seed_a < fromto.a:
                    if seed_b >= fromto.a:
                        result.append((seed_a, fromto.a - 1))
                        seed_a = fromto.a
                    else:
                        result.append((seed_a, seed_b))
                        seed_a = None
                        break
                if seed_a <= fromto.b:
                    if seed_b <= fromto.b:
                        result.append(
                            (
                                fromto.to_a + (seed_a - fromto.a), #seed_a
                                fromto.to_a + (seed_b - fromto.a) #seed_b,
                            )
                        )
                        seed_a = None
                        break
                    else:
                        result.append(
                            (fromto.to_a + (seed_a - fromto.a), #seed_a
                             fromto.to_b)
                        )
                        seed_a = fromto.b + 1
            if seed_a != None:
                result.append((seed_a, seed_b))
            #print(result)

        return deepcopy(result)

    def map_seeds(seeds, almanac):
        for almanac_line in almanac:
            seeds = trans(seeds, almanac_line)
        return min(seeds)  # tbd

    mapping = []
    for line in lines[2:]:
        if line == "":
            continue
        if re.match("[a-z].+", line):
            mapping.append([])
        else:
            dest, src, length = map(int, line.split())
            mapping[-1].append(
                Fromto(
                    a=src,
                    b=src + length - 1,
                    to_a=dest,
                    to_b=dest + length - 1,
                )
            )

    for i, m in enumerate(mapping):
        mapping[i] = sorted(m, key=lambda x: x[0])

    seeds = list(map(int, lines[0].split()[1:]))
    seed_range = [
        (seeds[idx], seeds[idx] + seeds[idx + 1] - 1) for idx in range(0, len(seeds), 2)
    ]
    locations = map_seeds(sorted(seed_range, key=lambda x: x[0]), mapping)

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
    # 4917124

start_t = dt.datetime.now()

#main(test=True)
main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
