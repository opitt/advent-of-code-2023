# https://adventofcode.com/2023/day/4
import os

def solve(lines):
    result = 0
    for line in lines:
        win, my = line.split(": ")[1].split(" | ")
        wins, nums = set(win.split()), set(my.split())
        match = len(wins.intersection(nums))
        if match>0:
            value = 1
            for _ in range(match-1):
                value += value
            result+= value

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
    # 32001


#main(test=True)
main(test=False)
