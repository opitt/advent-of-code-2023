package day07

import (
	_ "embed"
	"sort"
)

//go:embed test.data
var Test []byte
var TestResult_1 = int64(6440)

//go:embed input.data
var Input []byte

func Day07_1(dataB []byte) (sum int64) {
	part := 0
	cards := loadCards(dataB, part)
	sort.Slice(cards, func(i, j int) bool {
		ci := cards[i].hand
		cj := cards[j].hand
		ti := ci.getSimpleType()
		tj := cj.getSimpleType()
		if ti != tj {
			return ti > tj
		}
		for k := 0; k < 5; k++ {
			si, oki := strengthOfCard[part][ci.cards[k]]
			sj, okj := strengthOfCard[part][cj.cards[k]]
			if !oki || !okj {
				panic("oops")
			}
			if si == sj {
				continue
			}
			return si < sj
		}
		panic("oops")
	})
	for rank, card := range cards {
		sum += (int64(rank) + 1) * card.bid
	}
	return sum
}
