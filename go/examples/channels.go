package main

import "fmt"

func main() {
	messages := make(chan string)

	// send value
	go func() {messages <- "ping"}()

	// receive value
	msg := <-messages
	fmt.Println(msg)

	// continue to receive: error
	msg = <-messages
	fmt.Println(msg)
}
