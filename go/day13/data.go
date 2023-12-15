package day13

import (
	"fmt"

	"AdventOfCode2023/internal/util"
)

type (
	fieldT struct {
		horL []string
		verL []string
	}
)

func loadData(dataB []byte) (fieldsL []fieldT) {
	lines := util.LoadLines(dataB)
	field := fieldT{}
	for _, line := range lines {
		if line == "" {
			addField(&field, &fieldsL)
			continue
		}
		field.horL = append(field.horL, line)
	}
	addField(&field, &fieldsL)
	return fieldsL
}

func addField(field *fieldT, fieldsL *[]fieldT) {
	field.verL = make([]string, len(field.horL[0]))
	for i := range field.horL {
		for j := range field.horL[i] {
			field.verL[j] += string(field.horL[i][j])
		}
	}
	*fieldsL = append(*fieldsL, *field)
	*field = fieldT{}
}

func (field fieldT) Print(msg string, args ...any) {
	fmt.Printf(field.String()+msg+"\n\n", args...)
	//if idxHor > 0 && idxVer > 0 {
	//	fmt.Printf("%shor: %d ver: %d\n\n", field, idxHor, idxVer)
	//}
}

func (field fieldT) String() (s string) {
	for _, l := range field.horL {
		s += l + "\n"
	}
	return s
}
