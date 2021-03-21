package main

import (
	"fmt"
	"time"
)

func main() {
	d := 10
	duration := time.Duration(d) * time.Second
	fmt.Println(duration.Seconds())
}
