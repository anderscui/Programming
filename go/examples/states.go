package main

import "fmt"

func main() {
	// declare a struct, The Mars Curiosity
	var curiosity struct{
		lat float64
		long float64
	}
	curiosity.lat = -4.5
	curiosity.long = 137
	fmt.Println(curiosity)

	
}
