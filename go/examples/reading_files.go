package main

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	// reading files requires checking most calls for errors.
	dat, err := ioutil.ReadFile("data.txt")
	check(err)
	fmt.Println(string(dat))

	// f is a pointer to file
	f, err := os.Open("data.txt")
	check(err)

	//b1 := make([]byte, 5)
	//// n1 is the num of bytes read
	//n1, err := f.Read(b1)
	//check(err)
	//fmt.Printf("%d bytes: %s \n", n1, string(b1[:n1]))

	// o2 is the new offset
	o2, err := f.Seek(6, 0)
	check(err)
	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: ", n2, o2)
	fmt.Printf("%v \n", string(b2[:n2]))

	// use io package
	o3, err := f.Seek(6, 0)
	check(err)
	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s \n", n3, o3, string(b3))

	// rewind
	_, err = f.Seek(0, 0)
	check(err)

	// use bufio package
	r4 := bufio.NewReader(f)
	b4, err := r4.Peek(6)
	check(err)
	fmt.Printf("5 bytes: %s \n", string(b4))

	f.Close()
}
