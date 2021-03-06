package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

func init() {
	rand.Seed(time.Now().UnixNano())
}

func main() {
	// an unbuffered channel
	court := make(chan int)
	wg.Add(2)

	go player("Nadal", court)
	go player("Djokovic", court)

	// start the set
	court <- 1

	wg.Wait()
}

func player(name string, court chan int) {
	defer wg.Done()

	for {
		ball, ok := <- court
		if !ok {
			// the chan is closed, so we won
			fmt.Printf("Player %s won \n", name)
			return
		}

		n := rand.Intn(100)
		if n % 13 == 0 {
			fmt.Printf("Player %s missed \n", name)

			close(court)
			return
		}

		fmt.Printf("Player %s Hit %d\n", name, ball)
		ball++

		court <- ball
	}
}
