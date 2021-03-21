package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(id int, wg *sync.WaitGroup) {
	// notify this task is done
	defer wg.Done()

	// do this task
	fmt.Printf("Worker %d starting \n", id)
	time.Sleep(500 * time.Millisecond)
	fmt.Printf("Worker %d done \n", id)
}

func main() {
	var wg sync.WaitGroup

	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go worker(i, &wg)
	}
	// block until the WG counter goes back to 0
	wg.Wait()
}
