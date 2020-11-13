package main

import "fmt"

func main() {
	messages := make(chan string, 2)

	// send value
	messages <- "ping"
	messages <- "ping"
	// more sending: error
	messages <- "ping"

	// receive value
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
