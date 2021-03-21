package main

import (
	"fmt"
	"net/url"
	"strings"
)

func main()  {
	s := "http://mail.ciicsh.com:110"

	u, err := url.Parse(s)
	if err != nil {
		panic(err)
	}
	fmt.Println(u.Host, u.Port(), u.Scheme)

	fmt.Println(strings.Split("mail.ciicsh.com:110", ":")[0])
	fmt.Println(strings.Split("mail.ciicsh.com", ":")[0])
}