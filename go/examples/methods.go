package main

import "fmt"

type user struct {
	name string
	phone string
	email string
}

func (u user) changePhone (phone string) {
	u.phone = phone
}

func (u *user) changeEmail (email string) {
	u.email = email
}

func main() {
	u1 := user{name: "bill"}
	fmt.Println(u1)
	u1.changePhone("123")
	u1.changeEmail("a@b.c")
	fmt.Println(u1)

	u2 := &user{name: "claire"}
	fmt.Println(*u2)
	u2.changePhone("123")
	u2.changeEmail("a@b.c")
	fmt.Println(*u2)
}