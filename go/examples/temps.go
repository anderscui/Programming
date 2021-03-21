package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	f, err := ioutil.TempFile("", "temp")
	check(err)
	fmt.Println("temp file:", f.Name())
	defer os.Remove(f.Name())

	// write data
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	dname, err := ioutil.TempDir("", "sampledir")
	check(err)
	fmt.Println("temp dir:", dname)
	defer os.Remove(dname)

	fname := filepath.Join(dname, "file1")
	err = ioutil.WriteFile(fname, []byte{65, 66}, 0666)
	check(err)
}
