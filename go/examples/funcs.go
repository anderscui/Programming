package main

import "fmt"

// omit type
func plus(a, b int) int {
	return a + b
}

// multiple returning values
func add_sub(a, b int) (int, int) {
	return a+b, a-b
}

// variadic funcs
func sum(nums ...int) {
	fmt.Println(nums)

	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

// closure
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {
	res := plus(1, 2)
	fmt.Println("1 + 2 = ", res)

	add, sub := add_sub(3, 2)
	fmt.Println("add", add, "sub", sub)

	sum(1, 2, 3)
	nums := []int{1, 2, 3, 4}
	sum(nums...)

	nextInt := intSeq()
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())
}
