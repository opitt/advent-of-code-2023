package day01

import (
	"bufio"
	"bytes"
	_ "embed"
	"fmt"
	"strings"
)

//go:embed test-2.data
var Test_2 []byte

func Day01_2(dataB []byte) {
	sum := 0
	inbuf := bytes.NewBuffer(dataB)
	inscan := bufio.NewScanner(inbuf)
	for inscan.Scan() {
		lineS := strings.TrimSpace(inscan.Text())
		zA := findDigit(lineS, min, strings.Index, strings.IndexAny)
		zO := findDigit(lineS, max, strings.LastIndex, strings.LastIndexAny)
		num := zA*10 + zO
		sum += num
	}
	fmt.Printf("2023-1b: %d\n", sum)
}

func min(a, b int) bool {
	if b < 0 {
		return true
	}
	return a < b
}

func max(a, b int) bool {
	if b < 0 {
		return true
	}
	return a > b
}

func findDigit(lineS string, which func(int, int) bool, findSubStrIdx func(string, string) int, findAnyIdx func(string, string) int) int {
	digits := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	minIdx := findAnyIdx(lineS, "0123456789")
	minI := -1
	if minIdx >= 0 {
		minI = int(lineS[minIdx]) - int('0')
	}
	for i, digitS := range digits {
		idx := findSubStrIdx(lineS, digitS)
		if idx < 0 {
			continue
		}
		if which(idx, minIdx) {
			minIdx = idx
			minI = i + 1
		}
	}
	if minI < 0 || minI > 9 {
		panic("oops")
	}
	return minI
}
