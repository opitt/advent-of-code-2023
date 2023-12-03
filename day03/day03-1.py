# https://adventofcode.com/2023/day/3
import os
import re
from collections import namedtuple


def solve(input_lines):
    # extend the playing field to simplify indexing
    lines = ["." * len(input_lines)]
    lines.extend(input_lines)
    lines.append(lines[0])
    lines = [f".{line}." for line in lines]

    # find all numbers
    Partno = namedtuple("Partno", "value y x1 x2")
    numbers = []
    for y, line in enumerate(lines):
        matches = re.finditer("(\d+)", line)
        if matches:
            numbers.extend(
                [Partno(int(m.group()), y, m.start(), m.end() - 1) for m in matches]
            )

    # find all numbers, except the ones, that only touch a "."
    result = 0
    for partno in numbers:
        adjacent = lines[partno.y - 1][partno.x1 - 1 : partno.x2 + 2]
        adjacent += lines[partno.y][partno.x1 - 1]
        adjacent += lines[partno.y][partno.x2 + 1]
        adjacent += lines[partno.y + 1][partno.x1 - 1 : partno.x2 + 2]
        is_not_part = re.fullmatch("[\.]+", adjacent)
        if not is_not_part:
            result += partno.value

    return result


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
    # 540212


# main(test=True)
main(test=False)
