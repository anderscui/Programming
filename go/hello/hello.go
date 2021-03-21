package main

import (
	"fmt"
	"log"

	"andersc.com/greetings"
)

func main() {
	// Set properties of the predefined Logger.
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	// Get a greeting msg and print it.
	msg, err := greetings.Hello("Gladys")
	if err != nil {
		// print error and exit the program.
		log.Fatal(err)
	}

	fmt.Println(msg)
}
