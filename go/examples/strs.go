package main

import (
	"fmt"
	s "strings"
)

var p = fmt.Println

func main() {
	p("Contains: ", s.Contains("test", "es"))
	p("Count: ", s.Count("abcab", "ab"))
	p("HasPrefix: ", s.HasPrefix("abcde", "ab"))
	p("Index: ", s.Index("abcde", "ab"))
	p("Index: ", s.Index("abcde", "ba")) // -1
	p("Join: ", s.Join([]string{"a", "b"}, "-"))

	p("Replace: ", s.Replace("foo", "o",  "p", -1))
	p("Replace: ", s.Replace("foo", "o",  "p", 1))

	p("Split: ", s.Split("1-2-3", "-"))

	p("len: ", len("hello"))
	p("char: ", "hello"[1])
}
