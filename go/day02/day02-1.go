package day02

import (
	"bufio"
	"bytes"
	_ "embed"
	"fmt"
	"strings"

	"AdventOfCode2023/internal/util"
)

//go:embed test.data
var Test []byte

//go:embed input.data
var Input []byte

func Day02_1(dataB []byte) {
	maxCubesM := map[string]int64{
		"red":   12,
		"green": 13,
		"blue":  14,
	}
	sum := 0
	inbuf := bytes.NewBuffer(dataB)
	inscan := bufio.NewScanner(inbuf)
	gameNo := 1
	for inscan.Scan() {
		lineS := strings.TrimSpace(inscan.Text())
		l0L := strings.Split(lineS, ":")
		gamesL := strings.Split(l0L[1], ";")
		canAllGamesBeInBag := true
		for _, game := range gamesL {
			if !canCubesBeInBag(strings.TrimSpace(game), maxCubesM) {
				canAllGamesBeInBag = false
				break
			}
		}
		if canAllGamesBeInBag {
			sum += gameNo
		}
		gameNo++
	}
	fmt.Printf("2023-2a: %d\n", sum)
}

func canCubesBeInBag(game string, maxCubesM map[string]int64) bool {
	colors := map[string]bool{"red": true, "blue": true, "green": true}
	cubesL := strings.Split(game, ",")
	for _, cube := range cubesL {
		cL := strings.Split(strings.TrimSpace(cube), " ")
		colorName := cL[1]
		_, ok := colors[colorName]
		if !ok {
			panic("oops")
		}
		num := util.MustAtoi(cL[0])
		maxNum, ok := maxCubesM[colorName]
		if !ok {
			panic("oops")
		}
		if num > maxNum {
			return false
		}
	}
	return true
}
