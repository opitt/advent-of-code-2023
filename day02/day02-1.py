# https://adventofcode.com/2023/day/2
import os
import re


def solve(game_rounds, r_max=12, g_max=13, b_max=14):
    score = 0
    for round in game_rounds:
        game_id = int(round.split(":")[0].split()[1])
        r = map(lambda c: c <= r_max, map(
            int, re.findall("(\d+)(?= red)", round)))
        g = map(lambda c: c <= g_max, map(
            int, re.findall("(\d+)(?= green)", round)))
        b = map(lambda c: c <= b_max, map(
            int, re.findall("(\d+)(?= blue)", round)))

        score += game_id if all(r) and all(g) and all(b) else 0

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
    # 2505


# main(test=True)
main(test=False)
