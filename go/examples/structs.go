package main

import "fmt"

type Person struct {
	name string
	age int
}

// like a custom ctor
func newPerson(name string) *Person {
	p := Person{name: name}
	p.age = 42
	return &p
}

// receiver type of pointer
func (r *Person) learn() string {
	return "go"
}

// receiver type of pointer
func (r Person) book() string {
	return "The Go Programming Language"
}

func main() {
	fmt.Println(Person{"Bob", 20})
	fmt.Println(Person{ name: "Anders", age: 39})

	p := newPerson("Bill")
	fmt.Println(p)
	println(p.learn())
	println(p.book())
}