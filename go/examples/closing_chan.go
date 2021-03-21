package main

import "fmt"

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// worker goroutine, repeatedly receives from jobs.
	// more will be false if the chan is closed.
	// use more to notify `done` chan.
	go func() {
		for {
			j, more := <- jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// sends 3 jobs from main goroutine.
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// await the worker
	<-done
}
