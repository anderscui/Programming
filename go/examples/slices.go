package main

import "fmt"

func main() {
	s := make([]string, 3)
	s[0] = "a"
	fmt.Println(len(s), s)

	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println(len(s), s)

	// copy
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println(len(c), c)

	c[0] = "first"
	fmt.Println(s, c)

	// slice: [low, high]
	l := s[2:5]
	fmt.Println(len(l), l)

	l = s[:5]
	l = s[3:]
	fmt.Println(len(l), l)

	t := []string{"g", "h"}
	fmt.Println(len(t), t)
}
