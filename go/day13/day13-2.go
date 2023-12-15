package day13

import (
	_ "embed"
	"fmt"
)

var TestResult_2 = int64(400)

func Day13_2(dataB []byte) (sum int64) {
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
