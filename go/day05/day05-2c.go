package day05

import (
	"fmt"
	"sort"

	"AdventOfCode2023/internal/util"
)

func Day05_2c(dataB []byte) int64 {
	seeder, mprs := loadData(dataB)
	mappers := mprs.BackSort()
	loc := rangeT{
		start: 0,
		count: mappers.LocationUpperBound(),
	}
	for loc.start < mappers.LocationUpperBound() {
		seed, err := mappers.BackMapRange(loc)
		if err == nil && seeder.IsSeed(seed.start) {
			return loc.start
		}
		newStart := seed.start + seed.count
		loc = rangeT{
			start: newStart,
			count: mappers.LocationUpperBound() - newStart,
		}
	}
	return -1
}

type (
	rangeT struct {
		start int64
		count int64
	}
)

//func (mprs mappers) Draw() string {
//}
//
//func (mpr mapper) Draw() string {
//}

func (mprs mappers) Sort() (mappers mappers) {
	mappers = mprs
	for i, mpr := range mappers.mL {
		mappers.mL[i] = mpr.Sort()
	}
	return mappers
}

func (mpr mapper) Sort() mapper {
	mes := make([]mapEntry, len(mpr.mapEntries))
	copy(mes, mpr.mapEntries)
	sort.Slice(mes, func(i, j int) bool {
		return mes[i].src < mes[j].src
	})
	return mapper{
		mapEntries:       mes,
		tgtUpperBoundary: mpr.tgtUpperBoundary,
	}
}

func (mprs mappers) BackSort() (mappers mappers) {
	mappers = mprs
	for i, mpr := range mappers.mL {
		mappers.mL[i] = mpr.BackSort()
	}
	return mappers
}

func (mpr mapper) BackSort() mapper {
	mes := make([]mapEntry, len(mpr.mapEntries))
	copy(mes, mpr.mapEntries)
	sort.Slice(mes, func(i, j int) bool {
		return mes[i].tgt < mes[j].tgt
	})
	return mapper{
		mapEntries:       mes,
		tgtUpperBoundary: mpr.tgtUpperBoundary,
	}
}

func (mprs mappers) BackMapRange(loc rangeT) (*rangeT, error) {
	x := loc
	for i := len(mprs.mL) - 1; i >= 0; i-- {
		m := mprs.mL[i]
		y, err := m.BackMapRange(x)
		if err != nil {
			return nil, err
		}
		x = *y
	}
	return &x, nil
}

func (mpr mapper) BackMapRange(loc rangeT) (*rangeT, error) {
	x := loc
	for _, me := range mpr.mapEntries {
		if x.start < me.tgt {
			return &rangeT{
				start: x.start,
				count: me.tgt - x.start,
			}, nil
		}
		upperTgtBound := me.tgt + me.count
		if x.start < upperTgtBound {
			offset := x.start - me.tgt
			cnt := util.Min(me.count-offset, x.count)
			return &rangeT{
				start: me.src + offset,
				count: cnt,
			}, nil
		}
	}
	return nil, fmt.Errorf("dead end")
}
