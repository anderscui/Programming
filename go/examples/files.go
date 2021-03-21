package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
)

func readText(filePath string) string {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		panic(err)
	}
	return string(data)
}

func main() {
	wd, _ := os.Getwd()
	fmt.Println("working dir: ", wd)
	fmt.Println("working dir: ", filepath.Dir(wd))

	allSql := readText("./data/tables.sql")
	statements := strings.Split(allSql, "------SEP------")
	fmt.Println(len(statements), "statements")
	for _, stmt := range statements {
		fmt.Println(strings.TrimSpace(stmt))
		fmt.Println("------")
	}
}