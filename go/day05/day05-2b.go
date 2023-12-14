package day05

var TestResult_2 = int64(46)

func Day05_2b(dataB []byte) int64 {
	seeder, mappers := loadData(dataB)
	for loc := int64(0); loc < mappers.LocationUpperBound(); loc++ {
		seed := mappers.BackMap(loc)
		if seeder.IsSeed(seed) {
			return loc
		}
	}
	return -1
}

func (mprs mappers) BackMap(loc int64) int64 {
	x := loc
	for i := len(mprs.mL) - 1; i >= 0; i-- {
		m := mprs.mL[i]
		x = m.BackMap(x)
	}
	return x
}

func (mpr mapper) BackMap(loc int64) int64 {
	x := loc
	for _, me := range mpr.mapEntries {
		if x >= me.tgt && x < me.tgt+me.count {
			return me.src + x - me.tgt
		}
	}
	return loc
}
