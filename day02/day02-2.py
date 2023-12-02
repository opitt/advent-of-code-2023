# https://adventofcode.com/2023/day/2
import os
import re


def solve(game_rounds):
    score = 0
    for cubes in game_rounds:
        r = max(map(int,re.findall("(\d+)(?= red)", cubes)))
        g = max(map(int,re.findall("(\d+)(?= green)", cubes)))
        b = max(map(int,re.findall("(\d+)(?= blue)", cubes)))
        score += r*g*b
    return score


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines)
    print(
        f"The result is {result}."
    )
    # 70265


# main(test=True)
main(test=False)
