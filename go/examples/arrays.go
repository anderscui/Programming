package main

import "fmt"

func main() {
	var a [5]int
	fmt.Println("empty:", a, "of len", len(a))

	// declare and init
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println(b)
}