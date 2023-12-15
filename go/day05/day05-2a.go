package day05

import (
	"fmt"
	"runtime"
	"sync"
)

func AoC_2023_5b_par(dataB []byte) (result int64) {
	seeder, mappers := loadData(dataB)
	seedC := seeder.AllSeeds()
	locC := make(chan int64)
	var mapWG sync.WaitGroup
	jobs := runtime.NumCPU()
	//jobs = 1
	for i := 0; i < jobs; i++ {
		mapWG.Add(1)
		go func() {
			worker(seedC, mappers, locC)
			mapWG.Done()
		}()
	}
	var locWG sync.WaitGroup
	locWG.Add(1)
	go func() {
		cnt := 0
		minLocation := int64(-1)
		for loc := range locC {
			if minLocation < 0 || loc < minLocation {
				minLocation = loc
				fmt.Print("o")
			}
			cnt++
			if cnt%10_000_000 == 0 {
				fmt.Print(".")
			}
		}
		//fmt.Printf("2023-5b: %d\n", minLocation)
		result = minLocation
		locWG.Done()
	}()
	mapWG.Wait()
	close(locC)
	locWG.Wait()
	return result
}

func (sdr seeder) AllSeeds() <-chan int64 {
	numSeeds := int64(0)
	for _, se := range sdr.seedEntries {
		numSeeds += se.count
	}
	fmt.Printf("processing %d seeds ...\n", numSeeds)

	seedC := make(chan int64)
	go func() {
		for _, se := range sdr.seedEntries {
			for i := int64(0); i < se.count; i++ {
				seedC <- se.start + i
				//fmt.Print(",")
			}
		}
		//fmt.Println("closing seedC ...")
		close(seedC)
		//fmt.Println("closed seedC")
	}()
	return seedC
}

func worker(seedC <-chan int64, mappers mappers, locC chan<- int64) {
	for seed := range seedC {
		loc := mappers.Map(seed)
		locC <- loc
		//fmt.Print(";")
	}
	//fmt.Println("worker done")
}
