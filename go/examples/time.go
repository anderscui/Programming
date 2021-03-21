package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	now := time.Now()
	p(now)

	then := time.Date(2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	p(then.Year(), then.Month(), then.Day(), then.Nanosecond(), then.Location())
	p(then.Local())
	p(then.Date())
	p(then.Day(), then.Weekday())

	now.UnixNano()

	p(then.Before(now), then.After(now), then.Equal(now))

	diff := now.Sub(then)
	p(diff)
	p(then.Add(diff).Equal(now))

	dra := time.Duration(-1)
	println(dra.Nanoseconds())
}
