package day14

import (
	_ "embed"
	"fmt"
	"slices"

	"AdventOfCode2023/internal/util"
)

func Part2(dataB []byte) (sum int64) {
	pf := loadData(dataB)
	var sums []int64
	rest := 1_000_000_000 + 1000
	for i := 0; i < util.Min(1_000_000_000, rest); i++ {
		pf.Cycle()
		if rest > 1_000_000_000 {
			sums = append(sums, pf.SumRocks())
			if i > 15 {
				pl := findPeriodLen(sums)
				if pl > 0 {
					rest = i + 1 + (1_000_000_000-1-i)%pl
				}
			}
		}
	}
	//fmt.Printf("%+v\n", sums)
	return pf.SumRocks()
}

func findPeriodLen(sums []int64) (pl int) {
	sl := len(sums)
	for pl = 10; pl*2 < sl; pl++ {
		prd := sums[sl-pl : sl]
		prdPrev := sums[sl-pl*2 : sl-pl]
		if slices.Equal(prd, prdPrev) {
			return pl
		}
	}
	return 0
}

func (pf platformT) Cycle() {
	pf.TiltNorth()
	//pf.Print()
	pf.TiltWest()
	//pf.Print()
	pf.TiltSouth()
	//pf.Print()
	pf.TiltEast()
	//pf.Print()
	//fmt.Println()
}

func (pf platformT) Print() {
	for _, line := range pf.rocks {
		fmt.Println(string(line))
	}
	fmt.Println()
}

func (pf platformT) TiltNorth() {
	pf.Tilt(func(i, j int) (x, y int) {
		return j, i
	})
}

func (pf platformT) TiltWest() {
	pf.Tilt(func(i, j int) (x, y int) {
		return i, j
	})
}

func (pf platformT) TiltSouth() {
	h := len(pf.rocks)
	pf.Tilt(func(i, j int) (x, y int) {
		return h - j - 1, i
	})
}

func (pf platformT) TiltEast() {
	w := len(pf.rocks[0])
	h := len(pf.rocks)
	pf.Tilt(func(i, j int) (x, y int) {
		return w - i - 1, h - j - 1
	})
}

func (pf platformT) Tilt(coords func(int, int) (int, int)) {
	for i := 0; i < len(pf.rocks[0]); i++ {
		pf.TiltSlice(i, coords)
	}
}

func (pf platformT) TiltSlice(sn int, coords func(int, int) (int, int)) {
	offset := 0
	h := len(pf.rocks)
	for i := 0; i < h; i++ {
		x, y := coords(sn, i)
		switch pf.rocks[x][y] {
		case 'O':
			if offset > 0 {
				x1, y1 := coords(sn, i-offset)
				pf.rocks[x1][y1] = 'O'
				pf.rocks[x][y] = '.'
			}
		case '.':
			offset++
		case '#':
			offset = 0
		default:
			panic("oops")
		}
	}
}
