package main

import (
	"fmt"
	"sort"
)

func main() {
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	// sorting is in-place
	fmt.Println("Strings:", strs)

	sorted := sort.StringsAreSorted(strs)
	fmt.Println(sorted)
}
