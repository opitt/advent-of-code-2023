package day14

import (
	_ "embed"

	"AdventOfCode2023/internal/util"
)

//go:embed input.data
var Input []byte

type (
	platformT struct {
		rocks [][]byte
	}
)

func loadData(dataB []byte) (platform platformT) {
	lines := util.LoadLines(dataB)
	for _, line := range lines {
		platform.rocks = append(platform.rocks, []byte(line))
	}
	return platform
}

func (pf platformT) SumRocks() (sum int64) {
	for i := 0; i < len(pf.rocks[0]); i++ {
		sum += pf.SumCol(i)
	}
	return sum
}

func (pf platformT) SumCol(cn int) (sum int64) {
	h := len(pf.rocks)
	for i := 0; i < h; i++ {
		switch pf.rocks[i][cn] {
		case 'O':
			sum += int64(h - i)
		case '.':
		case '#':
		default:
			panic("oops")
		}
	}
	return sum
}
