package day05

import (
	"strings"

	"AdventOfCode2023/internal/util"
)

type (
	seeder struct {
		seedEntries []seedEntry
	}
	seedEntry struct {
		start, count int64
	}
)

func newSeeder(seedLineS string) (seeder seeder) {
	seedsS := strings.TrimSpace(strings.Split(seedLineS, ":")[1])
	seedsSL := strings.Split(seedsS, " ")
	for i := 0; i < len(seedsSL)/2; i++ {
		seeder.seedEntries = append(seeder.seedEntries, seedEntry{
			start: util.MustAtoi(seedsSL[2*i]),
			count: util.MustAtoi(seedsSL[2*i+1]),
		})
	}
	return seeder
}

func (sdr seeder) SimpleSeeds() <-chan int64 {
	seedC := make(chan int64)
	go func() {
		for _, se := range sdr.seedEntries {
			seedC <- se.start
			seedC <- se.count
		}
		//fmt.Println("closing seedC ...")
		close(seedC)
		//fmt.Println("closed seedC")
	}()
	return seedC
}

func (sdr seeder) IsSeed(seed int64) bool {
	for _, se := range sdr.seedEntries {
		if seed >= se.start && seed < se.start+se.count {
			return true
		}
	}
	return false
}
