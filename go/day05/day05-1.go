package day05

import (
	"bufio"
	"bytes"
	_ "embed"
	"strings"
)

//go:embed test.data
var Test []byte
var TestResult_1 = int64(35)

//go:embed input.data
var Input []byte

func Day05_1(dataB []byte) int64 {
	seeder, mappers := loadData(dataB)
	minLocation := int64(-1)
	for seed := range seeder.SimpleSeeds() {
		loc := mappers.Map(seed)
		if minLocation < 0 || loc < minLocation {
			minLocation = loc
		}
	}

	//fmt.Printf("2023-5a: %d\n", minLocation)
	return minLocation
}

func loadData(dataB []byte) (seeder seeder, mappers mappers) {
	inbuf := bytes.NewBuffer(dataB)
	inscan := bufio.NewScanner(inbuf)
	var mpr *mapper
	for inscan.Scan() {
		lineS := strings.TrimSpace(inscan.Text())
		switch {
		case strings.HasPrefix(lineS, "seeds: "):
			seeder = newSeeder(lineS)
		case strings.HasSuffix(lineS, " map:"):
			mpr = new(mapper)
		case lineS == "":
			mappers.Add(&mpr)
		default:
			mpr.Add(lineS)
		}
	}
	mappers.Add(&mpr)
	return seeder, mappers
}
