package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type response1 struct {
	Page int
	Fruits []string
}

// Fields must start with capital letters to be exported
type response2 struct {
	Page int	`json:"page"`
	Fruits []string	`json:"fruits"`
}

func main() {
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(slcB)
	fmt.Println(string(slcB))

	// encode custom types
	res1D := &response1{
		Page: 1,
		Fruits: []string{"apple", "peach"},
	}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// use tags to customize key names
	res2D := &response2{
		Page: 1,
		Fruits: []string{"apple", "peach"},
	}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// decode
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)
	// a map to hold data: str -> any type
	var dat map[string]interface{}
	if err := json.Unmarshal(byt, &dat); err != nil {
		panic(err)
	}
	fmt.Println(dat)

	// fields
	num := dat["num"].(float64)
	fmt.Println(num)

	// nested data requires a series of conversions
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// decode into custom types
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// encode to stdout
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"one": 10, "two": 20}
	enc.Encode(d)
}
