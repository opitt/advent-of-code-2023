package day14

import (
	_ "embed"
	"testing"

	"AdventOfCode2023/internal/util"
)

//go:embed test.data
var Test []byte
var TestResult_1 = int64(136)
var TestResult_2 = int64(64)

func TestPart1(t *testing.T) {
	util.CheckI64(TestResult_1, Part1(Test), "day 14 1 test", t)
}

func TestPart2(t *testing.T) {
	util.CheckI64(TestResult_2, Part2(Test), "day 14 2 test", t)
}
