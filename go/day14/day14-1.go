package day14

import (
	_ "embed"
)

func Part1(dataB []byte) (sum int64) {
	pf := loadData(dataB)
	pf.TiltNorth()
	sum = pf.SumRocks()
	return sum
}
