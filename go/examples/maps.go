package main

import "fmt"

func main() {
	m := make(map[string]int)
	m["one"] = 1
	m["two"] = 2
	fmt.Println(m)

	v1 := m["one"]
	fmt.Println("v1", v1)

	// len
	fmt.Println("len", len(m))

	// delete
	delete(m, "two")
	fmt.Println("len", len(m))

	_, prs := m["two"]
	fmt.Println("contains", prs)

	n := map[string]int{"three": 3, "four": 4, "five": 5}
	fmt.Println("map:", n)
}
