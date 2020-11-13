package main

import "fmt"

func main() {
	nums := []int{2, 3, 4}
	sum := 0
	// index and value for each entry
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	// for map, over key/value
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s \n", k, v)
	}

	// keys: 与预期不符
	for k := range kvs {
		fmt.Printf("%s \n", k)
	}

	// str：code points, not char
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
