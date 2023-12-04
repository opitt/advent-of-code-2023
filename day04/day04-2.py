# https://adventofcode.com/2023/day/4
import os


def solve(lines):
    cards = [1] * len(lines)
    for card, line in enumerate(lines):
        win_num, my_card = line.split(": ")[1].split(" | ")
        wins, nums = set(win_num.split()), set(my_card.split())
        match = len(wins.intersection(nums))
        if match > 0:
            for _ in range(cards[card]):
                for c in range(1, match + 1):
                    cards[card + c] += 1

    return sum(cards)


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
    # 5037841


# main(test=True)
main(test=False)
