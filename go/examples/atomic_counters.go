package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	// define a counter
	var ops uint64
	// help to wait for all goroutines
	var wg sync.WaitGroup

	// start 50 goroutines that each inc the counter 1000 times
	for i := 0; i < 50; i++ {
		// inc 1
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				//ops += 1 // a possible val: 30937
				atomic.AddUint64(&ops, 1)
			}
			// dec 1
			wg.Done()
		}()
	}
	// Wait blocks until the WaitGroup counter is zero.
	wg.Wait()
	fmt.Println("ops:", ops)
}
