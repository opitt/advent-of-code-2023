package day07

import (
	"fmt"
	"slices"
	"strings"

	"AdventOfCode2023/internal/util"
)

type (
	cardT     rune
	strengthT int
	handT     struct {
		cards [5]cardT
		s     string
		typ   handType
	}
	handBidT struct {
		hand handT
		bid  int64
	}
	handsT   []*handBidT
	handType int
)

const (
	None handType = iota
	FiveOfaKind
	FourOfaKind
	FullHouse
	ThreeOfaKind
	TwoPair
	OnePair
	HighCard
)

var cards = [2][]cardT{
	{'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'},
	{'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'},
}
var strengthOfCard = [2]map[cardT]strengthT{}

func loadCards(dataB []byte, part int) (hands handsT) {
	lines := util.LoadLines(dataB)
	strengthOfCard[part] = map[cardT]strengthT{}
	for i, c := range cards[part] {
		strength := len(cards[part]) - i + 1
		strengthOfCard[part][c] = strengthT(strength)
	}
	for _, line := range lines {
		hands = append(hands, newHand(line))
	}
	return hands
}

func newHand(line string) *handBidT {
	hbLS := strings.Split(line, " ")
	if len(hbLS) != 2 {
		panic("oops")
	}
	hand := handBidT{
		bid: util.MustAtoi(hbLS[1]),
	}
	if len(hbLS[0]) != 5 {
		panic("oops")
	}
	for i, cardR := range hbLS[0] {
		hand.hand.cards[i] = cardT(cardR)
	}
	hand.hand.s = hbLS[0]
	return &hand
}

func (hd handBidT) String() string {
	return hd.hand.s
}

func (hd handT) String() string {
	return hd.s
}

func (hd handT) toString() (s string) {
	for _, r := range hd.cards {
		s += string(r)
	}
	return fmt.Sprintf("%q t%d", s, hd.typ)
}

func (hd *handT) getSimpleType() handType {
	if hd.typ == None {
		hd.typ = hd.doGetSimpleType()
		hd.s = hd.toString()
	}
	return hd.typ
}

func (hd handT) hasJokers() bool {
	return slices.Contains(hd.cards[:], cardT('J'))
}

func (hd handT) doGetSimpleType() handType {
	sameCards := map[cardT]int{}
	for _, cd := range hd.cards {
		sameCards[cd]++
	}
	for _, cnt := range sameCards {
		switch {
		case cnt == 5 && len(sameCards) == 1:
			return FiveOfaKind
		case len(sameCards) == 2:
			switch {
			case cnt == 4:
				return FourOfaKind
			case cnt == 3:
				return FullHouse
			}
		case len(sameCards) == 3:
			switch cnt {
			case 1:
				continue
			case 3:
				return ThreeOfaKind
			case 2:
				return TwoPair
			}
		case len(sameCards) == 4:
			return OnePair
		case len(sameCards) == 5:
			return HighCard
		}
	}
	panic(fmt.Sprintf("oops: unknown card type: %+v", sameCards))
}

func (hd *handT) getJokerType() handType {
	if hd.typ == None {
		hd.typ = hd.doGetJokerType()
		hd.s = hd.toString()
	}
	return hd.typ
}

func (hd handT) doGetJokerType() handType {
	var hd2 = hd
	bestType := hd2.doGetSimpleType()
	for i, cd := range hd.cards {
		if cd != 'J' {
			continue
		}
		for _, cd2 := range cards[1] {
			hd3 := hd2
			hd3.setCard(i, cd2)
			t3 := hd3.doGetSimpleType()
			if t3 < bestType {
				bestType = t3
				hd2.setCard(i, cd2)
			}
		}
	}
	t := hd2.doGetSimpleType()
	return t
}

func (hd *handT) setCard(i int, cd cardT) {
	hd.cards[i] = cd
	hd.s = hd.toString()
}
