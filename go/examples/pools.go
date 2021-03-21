package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int, results chan<-int) {
	for j := range jobs {
		fmt.Println("worker", id, "started job", j)
		time.Sleep(500 * time.Millisecond)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}
func main() {
	const nJobs = 5
	jobs := make(chan int, nJobs)
	results := make(chan int, nJobs)

	// start 3 workers
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// distribute 5 jobs
	for j := 1; j <= nJobs; j++ {
		jobs <- j
	}
	// no new jobs
	close(jobs)

	for a := 1; a <= nJobs; a++ {
		<-results
	}
}
