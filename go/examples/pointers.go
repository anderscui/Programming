package main

import "fmt"

func zeroval(i int) {
	i = 0
}

func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("init", i)

	zeroval(i)
	fmt.Println("val", i)

	zeroptr(&i)
	fmt.Println("ptr", i)

	// memory address
	fmt.Println("pointer", &i)
}
