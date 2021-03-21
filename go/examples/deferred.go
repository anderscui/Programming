package main

import (
	"fmt"
	"os"
)

func main() {
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err != nil {
		panic(err)
	}
	return f
}

func writeFile(file *os.File) {
	fmt.Println("writing")
	fmt.Println(file, "data")
}

func closeFile(file *os.File) {
	fmt.Println("closing")
	err := file.Close()
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %v \n", err)
		os.Exit(1)
	}
}