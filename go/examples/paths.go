package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {
	p := filepath.Join("/Users/andersc", "aliases.sh")
	fmt.Println("path:", p)

	fmt.Println(filepath.Join("/Users//andersc", "aliases.sh"))
	fmt.Println(filepath.Join("Users/andersc/../andersc", "aliases.sh"))

	// dir
	fmt.Println("dir: ", filepath.Dir(p))
	// file name
	fmt.Println("base: ", filepath.Base(p))

	filename := filepath.Base(p)
	ext := filepath.Ext(filename)
	// filename without ext
	fmt.Println(strings.TrimSuffix(filename, ext))

	fmt.Println("ext of test: ", filepath.Ext("test"))
	fmt.Println("ext of empty: ", filepath.Ext(""))

	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err != nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/test")
	if err != nil {
		panic(err)
	}
	// this is interesting
	fmt.Println(rel)
}
