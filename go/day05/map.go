package day05

import (
	"strings"

	"AdventOfCode2023/internal/util"
)

type (
	mappers struct {
		mL []mapper
	}
	mapper struct {
		mapEntries       []mapEntry
		tgtUpperBoundary int64
	}
	mapEntry struct {
		src, tgt, count int64
	}
)

func (mprs *mappers) Add(mpr **mapper) bool { // *mapper {
	if mpr == nil || *mpr == nil {
		return false
	}
	mprs.mL = append(mprs.mL, **mpr)
	*mpr = nil
	return true
}

func (mprs *mappers) LocationUpperBound() int64 {
	mpr := mprs.mL[len(mprs.mL)-1]
	return mpr.tgtUpperBoundary
}

func (mprs mappers) Map(src int64) int64 {
	x := src
	for _, m := range mprs.mL {
		x = m.Map(x)
	}
	return x
}

func (mpr *mapper) Add(line string) {
	numsL := strings.Split(strings.TrimSpace(line), " ")
	if len(numsL) != 3 {
		panic("oops")
	}
	me := mapEntry{
		src:   util.MustAtoi(numsL[1]),
		tgt:   util.MustAtoi(numsL[0]),
		count: util.MustAtoi(numsL[2]),
	}
	mpr.mapEntries = append(mpr.mapEntries, me)
	if me.tgt+me.count > mpr.tgtUpperBoundary {
		mpr.tgtUpperBoundary = me.tgt + me.count
	}
}

func (mpr mapper) Map(x int64) int64 {
	for _, me := range mpr.mapEntries {
		if x >= me.src && x < me.src+me.count {
			return me.tgt + x - me.src
		}
	}
	return x
}
