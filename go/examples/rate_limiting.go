package main

import (
	"fmt"
	"time"
)

func main() {
	// rate limiting: method 1
	reqs := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		reqs <- i
	}
	close(reqs)

	limiter := time.Tick(200 * time.Millisecond)
	for req := range reqs {
		// blocking on a receive from the limiter channel before serving each request
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// rate limiting: method 2
	burstyLimiter := make(chan time.Time, 3)
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			// add a new value each 200 ms
			burstyLimiter <- t
		}
	}()

	burstyReqs := make(chan int, 6)
	for i := 1; i <= 6; i++ {
		burstyReqs <- i
	}
	close(burstyReqs)

	for req := range burstyReqs {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
}
