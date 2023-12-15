package day06

import (
	"testing"

	"AdventOfCode2023/internal/util"
)

func TestDay06_1(t *testing.T) {
	util.CheckI64(TestResult_1, Day06_1(Test_1), "day 6 1 test", t)
}

func TestDay06_2(t *testing.T) {
	util.CheckI64(TestResult_2, Day06_2(Test_2), "day 6 2 test", t)
}
