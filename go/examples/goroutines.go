package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i:= 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}
func main() {
	// this goroutine will execute concurrently with the calling one.
	go f("goroutine")

	// anonymous func
	go func(msg string) {
		fmt.Println(msg)
	}("anonymous going")

	// direct call
	f("direct")
	time.Sleep(time.Second)
	fmt.Println("done")
}