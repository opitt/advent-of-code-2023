# https://adventofcode.com/2023/day/3
import os


def solve(input_lines):
    resut=0
    ...
    return result

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
    # ???


main(test=True)
#main(test=False)
