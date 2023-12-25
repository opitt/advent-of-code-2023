# https://adventofcode.com/2023/day/7
import os
import datetime as dt
from collections import Counter


def solve(lines):
    def is_five_of_a_kind(hand):
        # Five of a kind, where all five cards have the same label: AAAAA
        # Five of a kind, where all five cards have the same label: JJAJJ with joker
        c = Counter(hand)
        joker_rule = "J" in c and len(c) == 2
        return 5 in c.values() or joker_rule

    def is_four_of_a_kind(hand):
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        c = Counter(hand)
        joker_rule = "J" in c and any(v + c["J"] == 4 for k, v in c.items() if k != "J")
        return 4 in c.values() or joker_rule

    def is_full_house(hand):
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        c = Counter(hand)
        # 8822J <<
        # 822JJ
        # 82JJJ
        # 2345J
        joker_rule = list(c.values()).count(2) == 2 and c["J"] == 1
        return 3 in c.values() and 2 in c.values() or joker_rule

    def is_three_of_a_kind(hand):
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        c = Counter(hand)
        # simplified joker rule. 4 of a kind is better, therfore this function return false
        joker_rule = "J" in c and any(v + c["J"] == 3 for k, v in c.items() if k != "J")
        return 3 in c.values() or joker_rule

    def is_two_pair(hand):
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        c = Counter(hand)
        # KKQQ2
        # JJK23
        joker_rule = c["J"] == 2 and len(c) == 4
        return sum([1 for count in c.values() if count == 2]) == 2 or joker_rule

    def is_one_pair(hand):
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        c = Counter(hand)
        joker_rule = c["J"] == 1 and len(c) == 5
        return sum([1 for pair in c.values() if pair == 2]) == 1 or joker_rule

    def is_high_card(hand):
        # High card, where all cards' labels are distinct: 23456
        c = set(hand)
        return len(c) == 5

    def get_label(hand):
        labels = {
            7: "five of a kind",
            6: "four of a kind",
            5: "full house",
            4: "three of a kind",
            3: "two pairs",
            2: "one pair",
            1: "high card",
        }
        return labels[rank_it_1(hand)]

    def rank_it_1(hand):
        if is_five_of_a_kind(hand):
            return 7
        elif is_four_of_a_kind(hand):
            return 6
        elif is_full_house(hand):
            return 5
        elif is_three_of_a_kind(hand):
            return 4
        elif is_two_pair(hand):
            return 3
        elif is_one_pair(hand):
            return 2
        elif is_high_card(hand):
            return 1
        else:
            print(hand)

    def rank_it_2(hand):
        card_values = {
            "A": "m",
            "K": "l",
            "Q": "k",
            # "J": "j",
            "T": "i",
            "9": "h",
            "8": "g",
            "7": "f",
            "6": "e",
            "5": "d",
            "4": "c",
            "3": "b",
            "2": "a",
            "J": "J",
        }
        return "".join(card_values[c] for c in hand)

    hands = [[game.split()[0], int(game.split()[-1])] for game in lines]
    # sort based on hand type and then on card
    hands = [[hand, bid, rank_it_1(hand), rank_it_2(hand)] for hand, bid in hands]
    hands = sorted(hands, key=lambda h: (h[2], h[3]))
    # for hand in hands:
    #    print(hand[0], get_label(hand[0]), hand[2], hand[3])
    value = [i * h[1] for i, h in enumerate(hands, 1)]
    return sum(value)


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines)
    print(f"The result ({'Test' if test else 'Input'}) is {result}.")
    # 243101568


main(test=True)

start_t = dt.datetime.now()
main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
