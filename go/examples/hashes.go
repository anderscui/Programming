package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

func main() {
	s := "hello world"
	h := sha256.New()

	h.Write([]byte(s))
	bs := h.Sum(nil)

	fmt.Println(s)
	fmt.Println(hex.EncodeToString(bs))
}