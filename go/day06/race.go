package day06

import (
	"strings"

	"AdventOfCode2023/internal/util"
)

type (
	raceT struct {
		time     int
		distance int
	}
	racesT struct {
		races []raceT
	}
)

func loadRaces(dataB []byte) (races racesT) {
	lines := util.LoadLines(dataB)
	if len(lines) != 2 {
		panic("oops")
	}
	if !strings.HasPrefix(lines[0], "Time:") {
		panic("oops")
	}
	if !strings.HasPrefix(lines[1], "Distance:") {
		panic("oops")
	}

	for _, timeS := range strings.Split(lines[0], " ") {
		if timeS == "Time:" || timeS == "" {
			continue
		}
		race := raceT{
			time:     int(util.MustAtoi(timeS)),
			distance: 0,
		}
		races.races = append(races.races, race)
	}

	i := 0
	for _, distS := range strings.Split(lines[1], " ") {
		if distS == "Distance:" || distS == "" {
			continue
		}
		dist := util.MustAtoi(distS)
		races.races[i].distance = int(dist)
		i++
	}
	return races
}

func (race raceT) WinningPossibilities() (sum int64) {
	for startTime := 1; startTime < race.time; startTime++ {
		dist := startTime * (race.time - startTime)
		if dist > race.distance {
			sum++
		}
	}
	return sum
}
