package main

import (
	"fmt"
	"time"

	"AdventOfCode2023/day01"
	"AdventOfCode2023/day02"
	"AdventOfCode2023/day05"
)

func main() {
	day01.Day01_1(day01.Input)
	day01.Day01_2(day01.Input)
	day02.Day02_1(day02.Input)
	day02.Day02_2(day02.Input)
	run("day 05 1 naive    ", day05.Day05_1, day05.Input)
	//run("day 5 b parallel ", day5.AoC_2023_5b_par, static.Data2023_5_Input)
	run("day 05 2 backwards simple", day05.Day05_2b, day05.Input)
}

func run(msg string, f func([]byte) int64, data []byte) {
	start := time.Now()
	res := f(data)
	dur := time.Now().Sub(start)
	fmt.Printf("AoC 2023 %-50s:   %12d    in %v\n", msg, res, dur)
}
