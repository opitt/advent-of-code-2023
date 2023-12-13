package util

import (
	"strconv"
	"strings"
	"testing"
)

func MustAtoi(s string) int64 {
	num, err := strconv.ParseInt(strings.TrimSpace(s), 10, 64)
	if err != nil {
		panic(err)
	}
	return num
}

func CheckI64(exp, act int64, errMsg string, t *testing.T) {
	if exp == act {
		return
	}
	//fmt.Printf("%s: expected %d but got %d\n", errMsg, exp, act)
	t.Errorf("%s: expected %d but got %d\n", errMsg, exp, act)
}
