package day05_test

import (
	"testing"

	"AdventOfCode2023/day05"
	"AdventOfCode2023/internal/util"
)

func TestDay05_1(t *testing.T) {
	util.CheckI64(day05.TestResult_1, day05.Day05_1(day05.Test), "day 5 a test", t)
}

func TestDay05_2_par(t *testing.T) {
	util.CheckI64(day05.TestResult_2, day05.AoC_2023_5b_par(day05.Test), "day 5 b 1 test", t)
}

func TestDay05_2_back(t *testing.T) {
	util.CheckI64(day05.TestResult_2, day05.Day05_2b(day05.Test), "day 5 b 2 test", t)
}

//func TestDay05_2_backRange(t *testing.T) {
//	util.CheckI64(day05.TestResult_2, day05.Day05_2c(day05.Test), "day 5 b 2 test", t)
//}
