package main

import (
	"fmt"
	"time"

	"AdventOfCode2023/day01"
	"AdventOfCode2023/day02"
	"AdventOfCode2023/day05"
	"AdventOfCode2023/day06"
	"AdventOfCode2023/day07"
	"AdventOfCode2023/day13"
	"AdventOfCode2023/day14"
)

func main() {
	day01.Day01_1(day01.Input)
	day01.Day01_2(day01.Input)
	day02.Day02_1(day02.Input)
	day02.Day02_2(day02.Input)
	run("day 05 1 naive", day05.Day05_1, day05.Input)
	//run("day 05 2 backwards simple", day05.Day05_2b, day05.Input)
	run("day 06 1 naive", day06.Day06_1, day06.Input_1)
	run("day 06 2 naive", day06.Day06_2, day06.Input_2)
	run("day 07 1", day07.Day07_1, day07.Input)
	run("day 07 2", day07.Day07_2, day07.Input)
	run("day 13 1", day13.Day13_1, day13.Input)
	run("day 14 1", day14.Part1, day14.Input)
	run("day 14 2", day14.Part2, day14.Input)
}

func run(msg string, f func([]byte) int64, data []byte) {
	start := time.Now()
	res := f(data)
	dur := time.Now().Sub(start)
	fmt.Printf("AoC 2023 %-50s:   %12d    in %v\n", msg, res, dur)
}
