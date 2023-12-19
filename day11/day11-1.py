# https://adventofcode.com/2023/day/11
import os
import datetime as dt
from itertools import combinations
from copy import deepcopy

def solve(lines):
    
    def expand_universe(universe):
        expanded_universe1 = []
        for line in universe:
            if line.count(".") == len(line):
                expanded_universe1.append(deepcopy(line))
                expanded_universe1.append(deepcopy(line))
            else:
                expanded_universe1.append(deepcopy(line))
        universe = ["".join(c for c in line[::-1]) for line in zip(*expanded_universe1)]
        expanded_universe1 = []
        for line in universe:
            if line.count(".") == len(line):
                expanded_universe1.append(line)
                expanded_universe1.append(line)
            else:
                expanded_universe1.append(line)
        return expanded_universe1

    def calc_distance(galaxy_pair):
        g1 = galaxy_pair[0] # (y,x)
        g2 = galaxy_pair[1] # (y,x)
        return abs(g1[1] - g2[1]) + abs(g1[0] - g2[0])
        
    def find_galaxies(universe):
        galaxies=[]
        for y, row in enumerate(universe):
            for x, c in enumerate(row):
                if c=="#":
                    galaxies.append((y,x))
        return galaxies
    
    expanded_universe = expand_universe(lines)
    galaxies = find_galaxies(expanded_universe)
    return sum([calc_distance(pair) for pair in combinations(galaxies,2)])

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
    # 9799681

start_t = dt.datetime.now()
main(test=True)

start_t = dt.datetime.now()
main(test=False)
end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")