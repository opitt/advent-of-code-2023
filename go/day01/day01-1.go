package day01

import (
	"bufio"
	"bytes"
	_ "embed"
	"fmt"
	"strings"
)

//go:embed test-1.data
var Test_1 []byte

//go:embed input.data
var Input []byte

func Day01_1(dataB []byte) {
	sum := 0
	inbuf := bytes.NewBuffer(dataB)
	inscan := bufio.NewScanner(inbuf)
	for inscan.Scan() {
		linsS := strings.TrimSpace(inscan.Text())
		idxA := strings.IndexAny(linsS, "0123456789")
		idxO := strings.LastIndexAny(linsS, "0123456789")
		zA := int(linsS[idxA]) - int('0')
		zO := int(linsS[idxO]) - int('0')
		num := zA*10 + zO
		sum += num
	}
	fmt.Printf("2023-1a: %d\n", sum)
}
