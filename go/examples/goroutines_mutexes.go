package main

import (
	"fmt"
	"runtime"
	"sync"
)

var (
	// updated by all goroutines
	counter int

	wg sync.WaitGroup

	mutex sync.Mutex
)

func main() {
	wg.Add(2)

	go incCounter(1)
	go incCounter(2)

	// wait for the goroutines to finish
	fmt.Println("Waiting to finish")
	wg.Wait()

	fmt.Printf("Final Counter: %d \n", counter)
}

func incCounter(i int) {
	// use mutex to provide safe access
	defer wg.Done()

	for count := 0; count < 2; count++ {
		// Only one goroutine can enter the critical section at a time.
		mutex.Lock()
		{
			value := counter
			// Gosched yields the processor, allowing other goroutines to run. It does not
			// suspend the current goroutine, so execution resumes automatically.
			runtime.Gosched()
			value++
			counter = value
		}
		mutex.Unlock()
	}
}