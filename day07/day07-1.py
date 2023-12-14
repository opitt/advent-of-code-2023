# https://adventofcode.com/2023/day/7
import os
import datetime as dt
from collections import Counter

def solve(lines):

    def is_five_of_a_kind(hand):
        #Five of a kind, where all five cards have the same label: AAAAA
        c = Counter(hand)
        return 5 in c.values()

    def is_four_of_a_kind(hand):
        #Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        c = Counter(hand)
        return 4 in c.values()

    def is_full_house(hand):
        #Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        c = Counter(hand)
        return 3 in c.values() and 2 in c.values()

    def is_three_of_a_kind(hand):
        #Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        c = Counter(hand)
        return 3 in c.values()

    def is_two_pair(hand):
        #Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        c = Counter(hand)
        return sum([1 for pair in c.values() if pair==2])==2

    def is_one_pair(hand):
        #One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        c = Counter(hand)
        return sum([1 for pair in c.values() if pair==2])==1

    def is_high_card(hand):
        #High card, where all cards' labels are distinct: 23456
        c = set(hand)
        return len(c)==5

    def rank_it_1(hand):
        if is_five_of_a_kind(hand):return 7
        elif is_four_of_a_kind(hand): return 6
        elif is_full_house(hand): return 5
        elif is_three_of_a_kind(hand): return 4
        elif is_two_pair(hand): return 3
        elif is_one_pair(hand): return 2
        elif is_high_card(hand): return 1
        else: print(hand)

    def rank_it_2(hand):
        card_values = {"A": "m", "K":"l" , "Q": "k", "J": "j", "T": "i", "9": "h", "8": "g", "7": "f", "6": "e", "5": "d", "4": "c", "3": "b", "2": "a"}
        return "".join(card_values[c] for c in hand)

    hands = [[game.split()[0], int(game.split()[-1])] for game in lines]
    # sort based on hand type and then on card
    hands = [[hand, bid, rank_it_1(hand), rank_it_2(hand)] for hand, bid in hands]
    hands = sorted(hands, key=lambda h: (h[2],h[3]))
    value = [ i*h[1] for i,h in enumerate(hands, 1)]
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
    print(f"The result is {result}.")
    # 241344943

start_t = dt.datetime.now()

#main(test=True)
main(test=False)

end_t = dt.datetime.now()
print(f"Runtime: {(end_t-start_t).total_seconds()}")
