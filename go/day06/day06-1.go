package day06

import (
	_ "embed"
)

//go:embed test-1.data
var Test_1 []byte
var TestResult_1 = int64(288)

//go:embed input-1.data
var Input_1 []byte

func Day06_1(dataB []byte) (product int64) {
	races := loadRaces(dataB)
	product = 1
	for _, race := range races.races {
		product *= race.WinningPossibilities()
	}
	return product
}
