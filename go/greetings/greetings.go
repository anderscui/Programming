package greetings

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

// Hello returns a greeting for the named person.
func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}

	// Return a greeting that embeds the name in a msg.
	msg := fmt.Sprintf(randomFormat(), name)
	return msg, nil
}

func init() {
	rand.Seed(time.Now().UnixNano())
}

func randomFormat() string {
	formats := []string{
		"Hi, %v. Welcome",
		"Great to see you, %v",
		"Hail, %v. Well met!",
	}

	return formats[rand.Intn(len(formats))]
}
