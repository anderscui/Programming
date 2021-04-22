package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	// only allocate 1 logical processor
	//runtime.GOMAXPROCS(1)
	fmt.Println(runtime.NumCPU(), "CPUs")
	runtime.GOMAXPROCS(2)

	// a counting semaphore
	var wg sync.WaitGroup
	wg.Add(2)

	fmt.Println("Start Goroutines")

	// goroutine 1
	go func() {
		// use closure
		defer wg.Done()

		for count := 0; count < 3; count++ {
			for char := 'a'; char < 'a' + 26; char++ {
				fmt.Printf("%c ", char)
			}
		}
	}()

	// goroutine 2
	go func() {
		defer wg.Done()

		for count := 0; count < 3; count++ {
			for char := 'A'; char < 'A' + 26; char++ {
				fmt.Printf("%c ", char)
			}
		}
	}()

	// wait for the goroutines to finish
	fmt.Println("Waiting to finish")
	wg.Wait()

	// the 1st goroutine is completed before swapping.
	fmt.Println("\nTerminating Program")
}