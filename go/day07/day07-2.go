package day07

import (
	_ "embed"
	"fmt"
	"sort"
)

var TestResult_2 = int64(5905)

func Day07_2(dataB []byte) (sum int64) {
	part := 1
	cards := loadCards(dataB, part)
	sort.Slice(cards, func(i, j int) bool {
		ci := cards[i].hand
		cj := cards[j].hand
		ti := ci.getJokerType()
		tj := cj.getJokerType()
		less := func() bool {
			if ti != tj {
				return ti > tj
			}
			for k := 0; k < 5; k++ {
				ki := ci.cards[k]
				kj := cj.cards[k]
				si, oki := strengthOfCard[part][ki]
				sj, okj := strengthOfCard[part][kj]
				if !oki || !okj {
					panic("oops")
				}
				if si == sj {
					continue
				}
				return si < sj
			}
			panic("oops")
		}()
		if ti == tj && (ci.hasJokers() || cj.hasJokers()) {
			s := fmt.Sprintf("%s  >  %s", ci, cj)
			if less {
				s = fmt.Sprintf("%s  <  %s", ci, cj)
			}
			_ = s
		}
		return less
	})
	for rank, card := range cards {
		sum += (int64(rank) + 1) * card.bid
	}
	return sum
}
