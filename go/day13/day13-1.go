package day13

import (
	_ "embed"
	"fmt"
)

//go:embed test.data
var Test []byte
var TestResult_1 = int64(405)

//go:embed input.data
var Input []byte

func Day13_1(dataB []byte) (sum int64) {
	fields := loadData(dataB)
	for _, field := range fields {
		idxHor := mirrorLineIdx(field.horL)
		if idxHor >= 0 {
			sum += int64(idxHor) * 100
		}
		idxVer := mirrorLineIdx(field.verL)
		if idxVer >= 0 {
			sum += int64(idxVer) // * 100
		}
		if idxHor < 0 && idxVer < 0 {
			for _, l := range field.horL {
				fmt.Println(l)
			}
		}
		//fmt.Printf("hi: %d, vi: %d\n\n", idxHor, idxVer)
	}
	return sum
}

func mirrorLineIdx(lines []string) (idx int) {
outerLoop:
	for i := range lines {
		if i > 0 && lines[i] == lines[i-1] {
			for j := 0; i-j > 0 && i+j < len(lines); j++ {
				if lines[i-j-1] != lines[i+j] {
					continue outerLoop
					//return -1
				}
			}
			return i
		}
	}
	return -1
}
