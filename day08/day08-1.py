# https://adventofcode.com/2023/day/8
import os
import datetime as dt
from itertools import cycle
import re

def solve(lines):
    instructions = cycle(lines[0])
    net = {}
    for line in lines[2:]:
        node, left, right = re.findall("[A-Z]+", line)
        net[node] = {"L":left, "R":right}

    node = "AAA"
    steps = 0
    for instruction in instructions:
        node = net[node][instruction]
        steps+=1
        if node=="ZZZ":
            break
    return steps
        
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
    # 23147

start_t = dt.datetime.now()

main(test=True)
#main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
