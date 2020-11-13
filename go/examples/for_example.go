package main

import "fmt"

func main() {
	// for a while
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i += 1
	}

	// conventional for
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// infinite loop
	for {
		fmt.Println("loop...")
		break
	}

	for n := 0; n <= 10; n++ {
		if n % 2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}