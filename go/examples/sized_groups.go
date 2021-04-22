package main

import (
	"fmt"
	"github.com/remeh/sizedwaitgroup"

	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	swg := sizedwaitgroup.New(2)
	for i := 0; i < 50; i++ {
		swg.Add()
		go func(i int) {
			defer swg.Done()
			query(i)
		}(i)
	}
}

func query(i int) {
	fmt.Println(i)
	ms := i + 500 + rand.Intn(500)
	time.Sleep(time.Duration(ms) * time.Millisecond)
}