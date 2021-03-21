package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// run: cat data.txt | go run line_filters.go
func main() {

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		// next token, here the line
		line := scanner.Text()
		fmt.Println(strings.ToUpper(line))
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}