# https://adventofcode.com/2023/day/4
import os


def solve(lines):
    cards = [1] * len(lines)
    for card, line in enumerate(lines):
        win_num, my_card = line.split(": ")[1].split(" | ")
        wins, nums = set(win_num.split()), set(my_card.split())
        match = len(wins.intersection(nums))
        if match > 0:
            # you win copies of the scratchcards below the winning card equal to the number of matches.
            # Copies of scratchcards are scored like normal scratchcards.
            # so if I now have 10 of card 5, I card 5 has 2 matches, I win 10x card 6 and 10x card 7.
            for c in range(1, match + 1):
                cards[card + c] += cards[card]

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
