package main

import "fmt"

// decalare a new type, not an alias
type celsius float64
type fahrenheit float64
type kelvin float64

// k is the `receiver`
func (k kelvin) celsius() celsius {
	return celsius(k - 273.15)
}

func (f fahrenheit) celsius() celsius {
	return celsius((f - 32.0) * 5.0 / 9.0)
}

func main() {
	var temperature celsius = 20
	fmt.Println(temperature)

	var k kelvin = 294.0
	c := k.celsius()
	fmt.Println(c)

	var f fahrenheit = 32.0
	c = f.celsius()
	fmt.Println(c)
}
