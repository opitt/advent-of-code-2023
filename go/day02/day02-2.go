package day02

import (
	"bufio"
	"bytes"
	"fmt"
	"strconv"
	"strings"
)

func Day02_2(dataB []byte) {
	sum := 0
	inbuf := bytes.NewBuffer(dataB)
	inscan := bufio.NewScanner(inbuf)
	for inscan.Scan() {
		lineS := strings.TrimSpace(inscan.Text())
		l0L := strings.Split(lineS, ":")
		game := l0L[1]
		maxCubesM := make(map[string]int)
		maxCubesInGame(game, maxCubesM)
		//cubesL := strings.Split(l0L[1], ";")
		//for _, game := range gamesL {
		//	maxCubesM := maxCubesInGame(game)
		power := 1
		for _, cubeCount := range maxCubesM {
			power *= cubeCount
		}
		sum += power
		//}
	}
	fmt.Printf("2023-2b: %d\n", sum)
}

func maxCubesInGame(game string, maxCubesM map[string]int) {
	//maxCubesM = make(map[string]int)
	colors := map[string]bool{"red": true, "blue": true, "green": true}
	cubesL := strings.Split(game, ";")
	for _, cubes := range cubesL {
		cubeL := strings.Split(cubes, ",")
		for _, cube := range cubeL {
			cL := strings.Split(strings.TrimSpace(cube), " ")
			colorName := cL[1]
			_, ok := colors[colorName]
			if !ok {
				panic("oops")
			}
			num, err := strconv.Atoi(strings.TrimSpace(cL[0]))
			if err != nil {
				panic(err)
			}
			if num > maxCubesM[colorName] {
				maxCubesM[colorName] = num
			}
		}
	}
	//return maxCubesM
}
