package main

import "fmt"

func main() {
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	// fatal error: all goroutines are asleep - deadlock!
	// queue <- "three"
	close(queue)

	// still can receive values from closed chan, like a seq
	for elem := range queue {
		fmt.Println(elem)
	}
}
