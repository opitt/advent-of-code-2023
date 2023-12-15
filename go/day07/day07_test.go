package day07

import (
	"testing"

	"AdventOfCode2023/internal/util"
)

func TestDay07_1(t *testing.T) {
	util.CheckI64(TestResult_1, Day07_1(Test), "day 07 1 test", t)
}

func TestDay07_2(t *testing.T) {
	util.CheckI64(TestResult_2, Day07_2(Test), "day 07 2 test", t)
}
